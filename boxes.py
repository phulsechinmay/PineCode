from rply.token import BaseBox

#region ------------------ Primitive Data Types ----------

class Integer(BaseBox):
    def __init__(self, val):
        self.value = int(val)
    
    def eval(self):
        if self.value:
            return self.value
        raise Exception("Not yet defined")

    def to_string(self):
        if self.value:
            return str(self.value)
        raise Exception("Not yet defined")
    
    def get_type(self):
        return "Integer"

class Float(BaseBox):
    def __init__(self, val):
        self.value = float(val)
    
    def eval(self):
        if self.value:
            return self.value
        raise Exception("Not yet defined")

    def to_string(self):
        if self.value:
            return str(self.value)
        raise Exception("Not yet defined")
    
    def get_type(self):
        return "Float"

class Bool(BaseBox):
    def __init__(self, val):
        self.value = bool(val)
    
    def eval(self):
        if self.value:
            return self.value
        raise Exception("Not yet defined")

    def to_string(self):
        if self.value:
            return str(self.value)
        raise Exception("Not yet defined")
    
    def get_type(self):
        return "Boolean"

class String(BaseBox):
    def __init__(self, val):
        self.value = str(val)
    
    def eval(self):
        if self.value:
            return self.value
        raise Exception("Not yet defined")

    def to_string(self):
        if self.value:
            return str(self.value)
        raise Exception("Not yet defined")
    
    def get_type(self):
        return "String"

#endregion

#region ------------------ Variables ------------

class Variable(BaseBox):
    def __init__(self, _name):
        self.name = str(_name)
        self.value = None
        self.type = None
 
    def getname(self):
        return str(self.name)

    # token : An object of type Token from the Lexer
    def setval(self, _value, _type): 
        self.value = _value
        self.type = _type
        return self
 
    def eval(self):
        if self.value:
            return self.value.eval()
        raise Exception("Not yet defined")
 
    def to_string(self):
        return str(self.name)
    
    def get_type(self):
        return self.type

#endregion

#region ------------------ Binary Operations ------------

class BinaryOperation(BaseBox):
    def __init__(self, left, right):
        self.left = left
        self.right = right
        self.type = self.left.get_type()

    def get_type(self):
        return self.type

class Add(BinaryOperation):
    def eval(self):
        return self.left.eval() + self.right.eval()

#endregion

#region ------------------ Helper Functions ------------

def Assignment(_variable_obj, _exp_val):
    if _exp_val:
        _variable_obj.setval(_exp_val.eval(), _exp_val.get_type())
    else:
        raise Exception(f"Variable assignment for {_variable_obj.getname()} with value {_exp_val.eval} was unsuccessful")

    return _variable_obj

#endregion