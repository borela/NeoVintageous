from .tokens import TOKEN_COMMAND_SHELL_OUT
from .tokens import TokenEof
from .tokens import TokenOfCommand
from NeoVintageous.nv import ex


@ex.command('!', '!')
class TokenShellOut(TokenOfCommand):
    def __init__(self, params, *args, **kwargs):
        super().__init__(params, TOKEN_COMMAND_SHELL_OUT, '!', *args, **kwargs)
        self.addressable = True
        self.target_command = 'ex_shell_out'

    @property
    def command(self):
        return self.params['cmd']


def scan_command_shell_out(state):
    params = {
        'cmd': None,
    }

    m = state.expect_match(r'(?P<cmd>.+)$')
    params.update(m.groupdict())

    return None, [TokenShellOut(params), TokenEof()]