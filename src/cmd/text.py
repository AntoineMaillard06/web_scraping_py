# module cmd text

def cmd_text(content):
    return content.get_text() + "\n_____\n"

def cmd_text_wordline(content, word):
    text = content.get_text().split('\n')
    response = word + " word match(s):\n"

    for line in text:
        if word.lower() in line.lower():
            response += line + '\n'
    response += "_____\n"
    return response

def cmd_text_wordlines(content, words):
    response = ""

    for word in words:
        response += cmd_text_wordline(content, word)
    return response

def cmd_text_element(content, element):
    text = content.find_all(element)
    response = element + " element(s) texts:\n"

    for line in text:
        response += str(line.string) + '\n'
    response += "_____\n"
    return response

def cmd_text_elements(content, elements):
    response = ""

    for element in elements:
        response += cmd_text_element(content, element)
    return response