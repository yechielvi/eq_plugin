
# implements_plugin.py
from typing import Callable
from mypy.types import Type
from mypy.plugin import Plugin, MethodContext

from implements import Implements
class ImplementPlugin(Plugin):
    def get_method_hook(self, fullname: str) -> Callable[[MethodContext], Type] | None:
        if fullname.endswith('.__eq__'):
            return proper_types_hook
        return None

def proper_types_hook(ctx: MethodContext) -> Type:
    other_ret_type = ctx.arg_types[0][0].type.get_method('__eq__').type.ret_type
    
    if not all(str(t).startswith('implements.Implements') for t in (ctx.default_return_type, other_ret_type)):
        return ctx.default_return_type
    
    if ctx.arg_types[0] not in ctx.default_return_type.args and ctx.type not in other_ret_type.args:
        ctx.api.fail('A not implement B and B not implement A', ctx.context)
    
    # need to replicate this type somewhere? to avoid # type: ignore[override]
    return ctx.api.named_generic_type('builtins.bool', [])


def plugin(version: str) -> type[ImplementPlugin]:
    return ImplementPlugin
