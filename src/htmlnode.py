class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props == None or self.props == {}:
            return ""
        result = ""
        for key in self.props:
            value = self.props[key]
            result += ' ' + key + '="' + value + '"'
         
        return result
    
    def __repr__(self):
        print(f"Tag:      {self.tag}")
        print(f"Value:    {self.value}")
        print(f"Children: {self.children}")
        print(f"Props:    {self.props}")

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag=tag, value=value, children=None, props=props)
        self.children = None

    def to_html(self):
        if self.value == None:
            raise ValueError
        if self.tag == None:
            return str(self.value)
        else:
            html_string = '<' + self.tag
            if self.props:
                html_string += self.props_to_html()
            html_string += '>' + self.value + '</' + self.tag + '>'
            return html_string
    
    def __repr__(self):
        print(f"Tag:      {self.tag}")
        print(f"Value:    {self.value}")
        print(f"Props:    {self.props}")