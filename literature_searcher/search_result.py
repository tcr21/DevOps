from flask import Blueprint, request, render_template, flash, send_file
from literature_searcher import query_processor
import sys
import subprocess

bp = Blueprint("search_result", __name__)


@bp.route("/search_result", methods=["GET", "POST"])
def response():
    query = request.args["search_query"]
    file_type = request.args["file_type"]

    if file_type == 'pdf':
        file_name = 'literature_searcher/results/result.md'
        args = ['pandoc', 'literature_searcher/results/result.md', '-o', 'literature_searcher/results/result.pdf', "--pdf-engine=pdflatex"]
        subprocess.run(args)
    else:
        file_name = 'literature_searcher/results/result.' + file_type

    if not query:
        flash("No query")
    search_results = query_processor.process(query)
    f = open(file_name, 'w')
    f.write(search_results[0])
    f.close()
    return render_template("search_result.html", search_results=search_results)


@bp.route("/download/<filetype>")
def download(filetype):
    file_name = 'results/result.' + filetype
    return send_file(file_name, as_attachment=True)
