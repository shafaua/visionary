
Visionary
=========

Python client library for Google Cloud Vision API

https://cloud.google.com/vision

Install
=======

Library can be installed with pip: `pip install visionary`


Usage
-----

Usage examples:

    from visionary import GoogleCloudVision, LabelDetection, LogoDetection
    
    API_KEY = "dummy_api_key"
    client = GoogleCloudVision(API_KEY)
    
    # Ask for logo detection, 10 results max
    response = client.annotate("dummy.jpg", LogoDetection())
    
    # Ask for label detection, 3 results max
    response = client.annotate("dummy.jpg", LabelDetection(3))

Detection params can be set explicitly:
    
    # 5 results max for logo detection and only one result for label detection
    response = client.annotate("dummy.jpg", LogoDetection(5), LabelDetection(1))

First param can be file object:
    
    uploaded_file = open("dummy.jpg")
    ...
    # somewhere later
    response = client.annotate(uploaded_file)
    
Or URL:    
    
    response = client.annotate("http://google.com/dummy.jpg")
    
Client supports multiple images in single `annotate` call

    response = client.annotate(
        ("dummy.jpg"),
        ("http://google.com/dummy.jpg"),
        ("dummy.jpg", LogoDetection(1)),
    )
    
Dealing with response:

    if response.ok:
        for resp in response.responses:
            for i in resp.logo_annotations:
                print(i.description)
    else:
        print(response.error['code'], response.error['message'], response.error['status'])

