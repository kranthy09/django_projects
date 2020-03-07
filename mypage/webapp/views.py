from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("this is webapp world, powered by django")

def time_stamp(request):
    import datetime
    res = str(datetime.datetime.now())
    return HttpResponse(f"current time stamp {res}")

def unique_id(request):
    import uuid
    res = str(uuid.uuid4())
    return HttpResponse(f"i'd: {res}")

def home_page(request):
    
    res = """<!DOCTYPE>
            <html>
                <body>
                    <h2>List 1</h2>
                    <ul>
                        <li>Team 1</li>
                        <li>Team 2</li>
                        <li>Team 3</li>
                    </ul>
                    <p>This is django world</p>
                </body>
            </html>
          """
    return HttpResponse(res)