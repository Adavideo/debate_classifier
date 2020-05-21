import csv, io

# PROCESS DATA

def process_news_without_author(column):
    title = column[4]
    content = column[5]
    text = "title: " + title + "\ncontent: " + content
    return text

def process_news_with_author(column):
    title = column[5]
    content = column[6]
    text = "title: " + title + "\ncontent: " + content
    return text

def process_comment(column):
    content = column[4]
    return content

def process_csv_line(column, file_type):
    if file_type == "news_without_author":
        result = process_news_without_author(column)
    elif file_type == "news_with_author":
        result = process_news_with_author(column)
    elif file_type == "comments":
        result = process_comment(column)
    else:
        result = "File type "+ str(file_type) + " not recognised"
    return result

def process_data(io_string, file_type):
    result = []
    for column in csv.reader(io_string, delimiter=',', quotechar='"'):
        r = process_csv_line(column, file_type)
        result.append(r)
    return result


# IDENTIFY FILE TYPE

def get_headers_types():
    headers_types = [ {"file_type":"news_without_author", "header": '"link_id","link_date","link_uri","link_url_title","link_title","link_content"'},
                      {"file_type":"news_with_author", "header": '"link_id","link_author","link_date","link_uri","link_url_title","link_title","link_content"'},
                      {"file_type":"comments", "header": '"comment_id","comment_link_id","comment_user_id","comment_date","comment_content"'},
                    ]
    return headers_types

def get_file_type(io_string):
    file_type = "incorrect"
    header = next(io_string)
    headers_types = get_headers_types()
    for header_type in headers_types:
        if header_type["header"] in header:
            file_type = header_type["file_type"]
    return file_type


# READ AND PROCESS CSV FILE

def process_csv(file):
    file_content = file.read().decode('UTF-8')
    io_string = io.StringIO(file_content)
    file_type = get_file_type(io_string)
    if file_type == "incorrect":
        result = ["Incorrect file type"]
    else:
        result = process_data(io_string, file_type)
    return result