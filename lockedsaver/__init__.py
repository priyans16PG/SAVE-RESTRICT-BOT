"""lockedsaver plugin wrappers — thin forwarders to the original cantarella modules.
This package enables renaming the plugins root while keeping original code intact.
"""

from importlib import import_module
__all__ = []
_mods = [
    'start', 'admin', 'strings', 'premium', 'session', 'settings',
    'caption', 'broadcast', 'thumbnail', 'words'
]
for m in _mods:
    try:
        mod = import_module(f'cantarella.{m}')
        globals().update({k: getattr(mod, k) for k in dir(mod) if not k.startswith('_')})
        __all__.extend([k for k in dir(mod) if not k.startswith('_')])
    except Exception:
        pass
