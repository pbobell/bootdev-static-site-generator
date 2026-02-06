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