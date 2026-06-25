from thing import main
import subprocess
import sys
import os


def compile_and_run_c(c_file, output_executable, extra_args=None):
    try:

        if extra_args is None:
            extra_args = []


        # Compile
        print(f"Compiling {c_file}...")

        compile_command = [
            "gcc",
            c_file,
            "-o",
            output_executable
        ] + extra_args


        result = subprocess.run(
            compile_command,
            capture_output=True,
            text=True
        )


        if result.returncode != 0:
            print("Compilation failed:")
            print(result.stderr)
            return


        print("Compilation successful!")


        # Run
        print(f"\nRunning {output_executable}...")
        print("--- Output ---")


        if sys.platform == "win32":
            run_command = output_executable + ".exe"
        else:
            run_command = "./" + output_executable


        result = subprocess.run(
            run_command,
            shell=True,
            capture_output=True,
            text=True
        )


        print(result.stdout)


        if result.stderr:
            print("--- Errors ---")
            print(result.stderr)


    except Exception as e:
        print("Error:", e)




def thing():

    # Your compiler/transpiler generates C here
    c_file = main()


    output_executable = os.path.splitext(c_file)[0]


    user_args = input(
        "Enter additional gcc arguments (comma separated): "
    ).strip()


    if user_args:
        args = [
            x.strip()
            for x in user_args.split(",")
        ]
    else:
        args = []


    compile_and_run_c(
        c_file,
        output_executable,
        args
    )



if __name__ == "__main__":
    thing()