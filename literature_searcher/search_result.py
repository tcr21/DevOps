from flask import Blueprint, request, render_template, flash
from literature_searcher import query_processor

bp = Blueprint("search_result", __name__)

@bp.route("/search_result", methods=["GET", "POST"])
def response():
    query = request.args["search_query"]
    file_type = request.args["file_type"]
    file_name = 'literature_searcher/results/'+query+'.'+file_type    
    #if 'download' in request.args:

    if not query:
        flash("No query")
    search_results = query_processor.process(query)
    f=open(file_name,'w')
    f.write(search_results[0])
    f.close()
    return render_template("search_result."+file_type, search_results=search_results)
