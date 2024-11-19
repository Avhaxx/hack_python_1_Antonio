"""
text: "fooziman" output => ["F","0","0","Z","1","M","@","N"]
"""

def fn_hack_10():
    result = "fooziman"
    output = []
    for char in result:
        if char == 'f':
            output.append('F')
        elif char == 'o':
            output.append('0')
        elif char == 'z':
            output.append('Z')
        elif char == 'i':
            output.append('1')
        elif char == 'm':
            output.append('M')
        elif char == 'a':
            output.append('@')
        elif char == 'n':
            output.append('N')
    return output