# Copyright (C) 2018 The NeoVintageous Team (NeoVintageous).
#
# This file is part of NeoVintageous.
#
# NeoVintageous is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# NeoVintageous is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with NeoVintageous.  If not, see <https://www.gnu.org/licenses/>.

from .tokens_base import *  # FIXME # noqa: F403


class TokenEof(Token):  # FIXME # noqa: F405
    def __init__(self, *args, **kwargs):
        super().__init__(TOKEN_EOF, '__EOF__', *args, **kwargs)  # FIXME # noqa: F405


class TokenOfSearch(TokenOfRange):  # FIXME # noqa: F405
    pass


class TokenDollar(TokenOfRange):  # FIXME # noqa: F405
    def __init__(self, *args, **kwargs):
        super().__init__(TOKEN_DOLLAR, '$', *args, **kwargs)  # FIXME # noqa: F405


class TokenComma(TokenOfRange):  # FIXME # noqa: F405
    def __init__(self, *args, **kwargs):
        super().__init__(TOKEN_COMMA, ',', *args, **kwargs)  # FIXME # noqa: F405


class TokenSemicolon(TokenOfRange):  # FIXME # noqa: F405
    def __init__(self, *args, **kwargs):
        super().__init__(TOKEN_SEMICOLON, ';', *args, **kwargs)  # FIXME # noqa: F405


class TokenOffset(TokenOfRange):  # FIXME # noqa: F405
    def __init__(self, content, *args, **kwargs):
        super().__init__(TOKEN_OFFSET, content, *args, **kwargs)  # FIXME # noqa: F405

    def __str__(self):
        offsets = []
        for offset in self.content:
            offsets.append('{0}{1}'.format('' if offset < 0 else '+', offset))

        return ''.join(offsets)


class TokenPercent(TokenOfRange):  # FIXME # noqa: F405
    def __init__(self, *args, **kwargs):
        super().__init__(TOKEN_PERCENT, '%', *args, **kwargs)  # FIXME # noqa: F405


class TokenDot(TokenOfRange):  # FIXME # noqa: F405
    def __init__(self, *args, **kwargs):
        super().__init__(TOKEN_DOT, '.', *args, **kwargs)  # FIXME # noqa: F405


class TokenSearchForward(TokenOfSearch):
    def __init__(self, content, *args, **kwargs):
        super().__init__(TOKEN_SEARCH_FORWARD, content, *args, **kwargs)  # FIXME # noqa: F405

    def __str__(self):
        return '/{0}/'.format(self.content)


class TokenSearchBackward(TokenOfSearch):
    def __init__(self, content, *args, **kwargs):
        super().__init__(TOKEN_SEARCH_BACKWARD, content, *args, **kwargs)  # FIXME # noqa: F405

    def __str__(self):
        return '?{0}?'.format(self.content)


class TokenDigits(TokenOfRange):  # FIXME # noqa: F405
    def __init__(self, content, *args, **kwargs):
        super().__init__(TOKEN_DIGITS, content, *args, **kwargs)  # FIXME # noqa: F405


class TokenMark(TokenOfRange):  # FIXME # noqa: F405
    def __init__(self, content, *args, **kwargs):
        super().__init__(TOKEN_MARK, content, *args, **kwargs)  # FIXME # noqa: F405

    def __str__(self):
        return "'{}".format(self.content)

    def __repr__(self):
        return "<[{0}]('{1})>".format(self.__class__.__name__, self.content)

    @property
    def exact(self):
        return self.content and self.content.startswith('`')
