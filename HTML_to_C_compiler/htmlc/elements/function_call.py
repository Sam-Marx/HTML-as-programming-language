from htmlc.elements.element import Element


class FunctionCall(Element):
    """"
    HTML:
    <funcname>
        <param ... />
        <param ... />
    </funcname>

    C: funcname(param1, param2, etc..);

    OR:
    HTML:   <funcname>10</funcname>
    C:      funcname(10);
    """

    def __init__(self):
        super().__init__()
        self.is_value_wrapper = True
        self.is_value = True

    def to_c(self, mapped_c):

        params = []
        # get params:
        for el in self.children:
            if el.tagname == "param":
                params.append(el.data.strip())

        if not len(params) and self.data:
            params = [self.data.strip()]

        c = "{}({})".format(  # for example: multiply(4, 5)
            self.tagname,
            ", ".join([param for param in params]))

        if not self.parent or not self.parent.is_value_wrapper:
            c += ";\n"

        mapped_c.add(c, self)

