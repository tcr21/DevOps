from flask import Blueprint, request, render_template, flash
from literature_searcher import query_processor

bp = Blueprint("search_result", __name__)

@bp.route("/search_result", methods=["GET", "POST"])
def response():
    query = request.args["search_query"]
    if not query:
        flash("No query")
    search_results = query_processor.process(query)
    return render_template("search_result.html", search_results=search_results)
