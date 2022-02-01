from re import search
from flask import Blueprint, request, render_template, flash, send_file, after_this_request
from literature_searcher import query_processor
import sys
import os
import subprocess

bp = Blueprint("search_result", __name__)


@bp.route("/search_result", methods=["GET", "POST"])
def response():
    query = request.args["search_query"]

    if not query:
        flash("No query")
    search_results = query_processor.process(query)
    if not search_results:
        return render_template("no_match.html")

    return render_template("search_result.html", search_results=search_results, query=query)


@bp.route("/download/<query>", methods=["GET", "POST"])
def download(query):
    file_type = request.args["file_type"]
    file_extension = '.md' if file_type == '.pdf' else file_type
    file_name = 'result' + file_extension
    search_results = query_processor.process(query)
    f = open("literature_searcher/"+file_name, 'w')
    for result in search_results:
        f.write(result)
        if file_type==".html":
            f.write("<br>")
        else:
            f.write("\n")

    f.close()

    if file_type == '.pdf':
        args = ['pandoc', 'literature_searcher/result.md', '-o',
                'literature_searcher/result.pdf', "--pdf-engine=pdflatex"]
        subprocess.run(args)
        file_name='result.pdf'
    
    @after_this_request
    def remove_file(response):
        try:
            os.remove("literature_searcher/" + file_name)
            if file_type == ".pdf":
                os.remove("literature_searcher/result.md")
        except Exception as error:
            print("Error removing or closing downloaded file handle", error)
        return response
    
    return send_file(file_name, as_attachment=True)
