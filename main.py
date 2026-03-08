# import argparse
# import sys
# import traceback

# from agent.flow import agent


# def main():
#     parser = argparse.ArgumentParser(description="Run engineering project planner")
#     parser.add_argument("--recursion-limit", "-r", type=int, default=100,
#                         help="Recursion limit for processing (default: 100)")

#     args = parser.parse_args()

#     try:
#         user_prompt = input("Enter your project prompt: ")
#         result = agent.invoke(
#             {"user_prompt": user_prompt},
#             {"recursion_limit": args.recursion_limit}
#         )
#         print("Final State:", result)
#     except KeyboardInterrupt:
#         print("\nOperation cancelled by user.")
#         sys.exit(0)
#     except Exception as e:
#         traceback.print_exc()
#         print(f"Error: {e}", file=sys.stderr)
#         sys.exit(1)


# if __name__ == "__main__":
#     main()



import streamlit as st
import zipfile
import os
import io
import traceback

from agent.flow import agent

GENERATED_FOLDER = "generated_project"


def zip_project(folder_path):
    """Zip the generated project folder"""
    zip_buffer = io.BytesIO()

    with zipfile.ZipFile(zip_buffer, "w", zipfile.ZIP_DEFLATED) as zip_file:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)

                arcname = os.path.relpath(file_path, folder_path)

                zip_file.write(file_path, arcname)

    zip_buffer.seek(0)
    return zip_buffer


st.set_page_config(page_title="Engineering Project Planner", layout="centered")

st.title("⚙️ Engineering Project Planner")

st.write("Generate complete engineering projects using AI")

prompt = st.text_area(
    "Enter your project prompt",
    height=150,
    placeholder="Example: Build a FastAPI backend for a todo application with PostgreSQL"
)

recursion_limit = st.slider(
    "Recursion Limit",
    min_value=10,
    max_value=500,
    value=100
)

generate = st.button("Generate Project")


if generate:

    if not prompt.strip():
        st.warning("Please enter a prompt")
        st.stop()

    with st.spinner("Generating project..."):

        try:

            result = agent.invoke(
                {"user_prompt": prompt},
                {"recursion_limit": recursion_limit}
            )

            st.success("Project generated successfully!")

            st.subheader("Final State")
            st.json(result)

            if os.path.exists(GENERATED_FOLDER):

                zip_file = zip_project(GENERATED_FOLDER)

                st.download_button(
                    label="Download Project",
                    data=zip_file,
                    file_name="generated_project.zip",
                    mime="application/zip"
                )

            else:
                st.error("Generated project folder not found.")

        except Exception as e:
            st.error("Error occurred during generation")
            st.text(traceback.format_exc())