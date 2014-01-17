###
# Copyright (c) 2014, Stacey Ell
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
#   * Redistributions of source code must retain the above copyright notice,
#     this list of conditions, and the following disclaimer.
#   * Redistributions in binary form must reproduce the above copyright notice,
#     this list of conditions, and the following disclaimer in the
#     documentation and/or other materials provided with the distribution.
#   * Neither the name of the author of this software nor the name of
#     contributors to this software may be used to endorse or promote products
#     derived from this software without specific prior written consent.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED.  IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

###

import random
import supybot.utils as utils
from supybot.commands import *
import supybot.plugins as plugins
import supybot.ircutils as ircutils
import supybot.callbacks as callbacks
try:
    from supybot.i18n import PluginInternationalization
    _ = PluginInternationalization('Fetwgrkifg')
except ImportError:
    # Placeholder that allows to run the plugin on a bot
    # without the i18n module
    _ = lambda x:x


def the_mangler_factory(map=map, chr=chr):
    maybe_bytes = lambda x: x
    if isinstance(map(lambda x: x, []), list):  # python2 shims
        map = __import__('itertools').imap
        chr = unichr
        maybe_bytes = lambda x: map(ord, x)
    return (lambda x: u''.join(map(chr, map(__import__('operator').and_, maybe_bytes(x.encode('utf8')), map(lambda x: x ^ 0xFF, __import__('itertools').cycle([0, 0, 0, 8]))))))


class Fetwgrkifg(callbacks.Plugin):
    """Add the help for "@plugin help Fetwgrkifg" here
    This should describe *how* to use this plugin."""

    def doPrivmsg(self, irc, msg):
        if ircmsgs.isCtcp(msg) and not ircmsgs.isAction(msg):
            return
        (channel, text) = msg.args
        if not irc.isChannel(channel):
            return
        if random.randint(0, 1000) < 3:
            irc.reply(the_mangler_factory()(text), prefixNick=False)


Class = Fetwgrkifg


# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:
