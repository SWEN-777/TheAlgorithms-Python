import os
import ast
import doctest
import coverage
import importlib
import sys
import io
import subprocess

def has_doctest(file_path):
    """Check if a Python file contains doctest examples."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            tree = ast.parse(f.read(), filename=file_path)
        for node in ast.walk(tree):
            if isinstance(node, (ast.FunctionDef, ast.ClassDef, ast.Module)):
                docstring = ast.get_docstring(node)
                if docstring and ">>>" in docstring:
                    return True
    except Exception as e:
        print(f"⚠️ Error parsing {file_path}: {e}")
    return False

def run_doctest_with_coverage(file_path, project_root):
    print(f"\n📄 Running doctests in: {file_path}")

    if project_root not in sys.path:
        sys.path.insert(0, project_root)

    rel_path = os.path.relpath(file_path, project_root)
    module_name = rel_path.replace(os.sep, ".").rstrip(".py")

    cov = coverage.Coverage(source=[os.path.dirname(file_path)], include=[file_path])
    cov.start()

    try:
        module = importlib.import_module(module_name)
        result = doctest.testmod(module)
    except Exception as e:
        print(f"❌ Import failed for {file_path}: {e}")
        cov.stop()
        cov.save()
        return {
            "type": "doctest",
            "file": file_path,
            "passed": 0,
            "failed": 1,
            "coverage": 0
        }

    cov.stop()
    cov.save()

    try:
        analysis = cov.analysis(file_path)
        covered = len(analysis[1])
        missed = len(analysis[3])
        buffer = io.StringIO()
        percent = cov.report(file=buffer, show_missing=False)
        buffer_output = buffer.getvalue()
        buffer.close()
    except Exception as e:
        print(f"⚠️ Coverage analysis failed for {file_path}: {e}")
        covered = missed = percent = 0

    print(f"✅ Passed: {result.attempted - result.failed}, ❌ Failed: {result.failed}")
    print(f"📊 Coverage: {percent:.1f}%")
    return {
        "type": "doctest",
        "file": file_path,
        "passed": result.attempted - result.failed,
        "failed": result.failed,
        "coverage": percent
    }

def run_pytest_with_coverage(pytest_dir):
    print(f"\n🧪 Running pytest in: {pytest_dir}")

    subprocess.run([
        "coverage", "run", "--parallel-mode", "-m", "pytest", pytest_dir,
        "--tb=short", "--disable-warnings"
    ])

    subprocess.run(["coverage", "combine"])

    try:
        report = subprocess.run(
            ["coverage", "report"],
            capture_output=True,
            text=True
        )
        output = report.stdout
        print(output)

        lines = output.strip().splitlines()
        last_line = lines[-1] if lines else ""
        percent = float(last_line.split()[-1].replace("%", "")) if "%" in last_line else 0.0
    except Exception as e:
        print(f"⚠️ Coverage analysis failed for {pytest_dir}: {e}")
        percent = 0.0

    print(f"📊 Coverage: {percent:.1f}%")
    return {
        "type": "pytest",
        "file": pytest_dir,
        "passed": "see output",
        "failed": "see output",
        "coverage": percent
    }

def run_all_tests(doctest_dirs, pytest_dirs, project_root):
    summary = []

    for parent_directory in doctest_dirs:
        for dirpath, _, filenames in os.walk(parent_directory):
            for filename in filenames:
                if filename.endswith(".py"):
                    file_path = os.path.join(dirpath, filename)
                    if has_doctest(file_path):
                        result = run_doctest_with_coverage(file_path, project_root)
                        summary.append(result)

    for test_dir in pytest_dirs:
        result = run_pytest_with_coverage(test_dir)
        summary.append(result)

    print("\n📋 Combined Summary Report")
    for item in summary:
        label = "🧪 Pytest" if item["type"] == "pytest" else "📄 Doctest"
        print(f"{label} - {item['file']}: ✅ {item['passed']} ❌ {item['failed']} 📊 {item['coverage']:.1f}%")

if __name__ == "__main__":
    project_root = "/Users/uzairmukadam/Projects/TheAlgorithms-Python"

    doctest_dirs = [
        f"{project_root}/data_structures/",
    ]

    pytest_dirs = [
        f"{project_root}/data_structures/",
    ]

    run_all_tests(doctest_dirs, pytest_dirs, project_root)
