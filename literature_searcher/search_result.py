from flask import Blueprint, request, render_template, flash, send_file, after_this_request
from literature_searcher import query_processor
import sys
import os
import subprocess

bp = Blueprint("search_result", __name__)


@bp.route("/search_result", methods=["GET", "POST"])
def response():
    query = request.args["search_query"]
    file_type = request.args["file_type"]

    if not query:
        flash("No query")
    search_results = query_processor.process(query)

    file_path = 'literature_searcher/results/result.'
    file_extension = 'md' if file_type == 'pdf' else file_type
    file_name = file_path + file_extension

    f = open(file_name, 'w')
    f.write(search_results[0])
    f.close()

    if file_type == 'pdf':
        args = ['pandoc', 'literature_searcher/results/result.md', '-o', 'literature_searcher/results/result.pdf', "--pdf-engine=pdflatex"]
        subprocess.run(args)
  
    return render_template("search_result.html", search_results=search_results, file_type=file_type)

@bp.route("/download/<filetype>")
def download(filetype):
    file_name = 'results/result.' + filetype

    @after_this_request
    def remove_file(response):
        try:
            os.remove("literature_searcher/" + file_name)
            if filetype == "pdf":
                os.remove("literature_searcher/results/result.md")
        except Exception as error:
            print("Error removing or closing downloaded file handle", error)
        return response

    return send_file(file_name, as_attachment=True)
