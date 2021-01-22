import uuid
import re

def create_uuid(hex=True):
    res=uuid.uuid4()
    return res.hex if hex else str(res)

def copy_function_with_params(fcn, add_args=None, **kwargs):
    if add_args is None: add_args=[]
    if type(add_args) not in [list,tuple]: add_args=[add_args]
    new_args={key:val for key,val in kwargs.items() if key in fcn.__code__.co_varnames}
    varnames=add_args+[x for x in fcn.__code__.co_varnames if x not in new_args and x not in add_args]
    defaults={x:fcn.__defaults__[i] for i,x in enumerate(fcn.__code__.co_varnames[fcn.__code__.co_argcount-len(fcn.__defaults__):]) if x in varnames}
    fcn_args=add_args+[x for x in fcn.__code__.co_varnames[:fcn.__code__.co_argcount-len(fcn.__defaults__)] if x in varnames]
    def y():
        mylocals=locals()
        vars={x:mylocals.get(x) for x in varnames}
        vars.update(new_args)
        args=[vars[x] for x in fcn_args]
        kwargs={key:val for key,val in vars.items() if key not in fcn_args}
        return fcn(*args,**kwargs)

    #code(argcount, kwonlyargcount, nlocals, stacksize, flags, codestring,constants, names, varnames, filename, name, firstlineno,lnotab[, freevars[, cellvars]])
    fcn_code = types.CodeType(len(varnames),
                            y.__code__.co_kwonlyargcount,
                            y.__code__.co_nlocals,
                            y.__code__.co_stacksize,
                            y.__code__.co_flags,
                            y.__code__.co_code,
                            y.__code__.co_consts,
                            y.__code__.co_names,
                            tuple(varnames),
                            y.__code__.co_filename,
                            fcn.__code__.co_name,
                            y.__code__.co_firstlineno,
                            y.__code__.co_lnotab,
                            y.__code__.co_freevars,
                            y.__code__.co_cellvars)

    res=types.FunctionType(fcn_code, {**fcn.__globals__,**y.__globals__}, fcn.__code__.co_name,
                            argdefs=tuple([defaults[key] for key in varnames if key in defaults]),
                            closure=y.__closure__)
    res.__doc__=fcn.__doc__

    return res

def iterable(l):
    try:
        iter(l)
        return True
    except:
        return False

def natural_sort(l,by=None):
    convert = lambda text: int(text) if text.isdigit() else text.lower()

    pos=None
    if iterable(by) and len(by)==len(l):
        l=zip(l,by)
        pos=1
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key if pos is None else key[pos]) ]
    res=sorted(l, key = alphanum_key)
    if pos is not None: res=list(zip(*res))[0]
    return res
