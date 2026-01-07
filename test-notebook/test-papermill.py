# /// script
# dependencies = ["papermill", "ipykernel"]
# ///

import papermill as pm

pm.execute_notebook(
    input_path="/Users/gauravwaghmare/Documents/Personal/spark-notebook-examples/test-notebook/test-spark.ipynb",
    output_path="/Users/gauravwaghmare/Documents/Personal/spark-notebook-examples/test-notebook/test-spark-output.ipynb",
    kernel_name="python",
    cwd="/Users/gauravwaghmare/Documents/Personal/spark-notebook-examples",
)
