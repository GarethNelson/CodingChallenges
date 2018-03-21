from functools import wraps,partial

# end continuation
end_cont   = lambda _endcont_retval: _endcont_retval
# call without trampoline
no_tramp   = lambda f,*args,**kwargs: f.orig_func(*args,**kwargs,_cont=end_cont)
# utility function for doing no_tramp with simpler syntax
_me        = lambda f: partial(no_tramp,f)
# return this to do a tail call
tailcall   = lambda f,*args,**kwargs: lambda: _me(f)(*args,**kwargs)
# used by a function to iterate over a sequence safely when returning, for infinitely deep nested lists, syntax+params are same as map(func,seq)
map_self   = lambda _ms_f,_ms_l: map(_me(_ms_f),_ms_l)
# convenience function for returning a list from map_self
lmap_self  = lambda _ms_f,_ms_l: list(map_self(_ms_f,_ms_l))
# convenience function for mapping different functions/lambda expressions to key+value of passed in dictionary item or similar sequence of pairs
map_items  = lambda _ms_kf,_ms_vf,_ms_l: [[_ms_kf(_ms_k),_ms_vf(_ms_v)] for _ms_k,_ms_v in _ms_l]
# same as above, but uses same function for both key+val and assumes it's a self call
map_self_both = lambda _msb_f,_msb_l: map_items(_me(_msb_f),
                                                _me(_msb_f),_msb_l)

# like map_items but where keys are a call to self
map_self_keys = lambda _msk_kf,_msk_vf,_msk_l: map_items(_me(_msk_kf),
                                                         _msk_vf,
                                                         _msk_l)

# map_items, but where values are a call to self
map_self_vals = lambda _msv_kf,_msv_vf,_msk_l: map_items(_msv_kf,
                                                         _me(_msv_vf),
                                                         _msk_l)


def trampwrap(f):
    """Wrap a function in a CPS trampoline
       The wrapped function must return values by using "return _cont(x)" or any valid lambda expression (this is how tail recursion is implemented safely)
    """

    @wraps(f)
    def fn(*args,**kwargs):
        v = f(*args,**kwargs)
        while callable(v):
           if v==f.tramp_func: v=f
           v = v()
        return v
    f.tramp_func = fn
    fn.orig_func = f
    return fn

