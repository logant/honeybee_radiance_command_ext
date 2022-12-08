"""Ies2rad parameters."""
from honeybee_radiance_command.options.optionbase import OptionCollection, FileOption, NumericOption, StringOption,\
    StringOptionJoined, TupleOption


class Ies2radOptions(OptionCollection):
    """
    ies2rad -m 1 -o %~dp0ies\temp\luminaire_%%a -c %cct% -dm %~dp0ies\sculpted\%scene%_LUM_%%a.ies
    [-m muliplier][-dunits][-l libdir][-p prefdir][-t lamp][-c red green blue][-f lampdat][-u lamp]

    Also see: https://floyd.lbl.gov/radiance/man_html/ies2rad.1.html
    """

    __slots__ = ('_l', '_p', '_d', '_f', '_t', '_c', '_u', '_m')

    def __init__(self):
        """Ies2rad command options."""
        OptionCollection.__init__(self)
        self._l = FileOption('l', 'library directory path', None)
        self._p = FileOption('p', 'library subdirectory path', None)
        self._d = StringOptionJoined('d', 'output units - default: meters', value='m')
        self._f = FileOption('f', 'custom lampdat file',None)
        self._t = StringOption('t', 'use the given lamp type', value='default')
        self._c = TupleOption('c', 'lamp color as red, green, and blue', None, 3, float)
        self._u = StringOption('u', 'set color by Lamp entry (see _f)', None)
        self._m = NumericOption('m', 'multiplier for output to scale brightness', value=1.0)
        # note this would maybe be useful when chaining with xform?
        # self._s = BoolOption('s', 'send to standard output rather than a file')
        # the -i switch is noted in the radiance docs to be 'obviated by recent LM-63-1995 spec'
        # self._i = NumericOption('i', 'illum sphere radius')
        # The IES files from Lumileds do not have an MGF file, so I'm ignoring for now.
        # self._g = BoolOption('g', 'compile Material and Geometry Format (MGF) to a separate octree'
        self._on_setattr_check = True

    def _on_setattr(self):
        """This method executes after setting each new attribute.

        Use this method to add checks that are necessary for OptionCollection. For
        instance in rtrace option collection -ti and -te are exclusive. You can include a
        check to ensure this is always correct.
        """
        # check if we need this.
        # assert not (self.b.is_set and self.i.is_set), \
        #    'The -b and -i options are mutually exclusive.'

    @property
    def l(self):
        """Specify the library directory path."""
        return self._l

    @l.setter
    def l(self, value):
        # TODO: verify 'value' is a directory
        self._l.value = value

    @property
    def p(self):
        """Specify the library subdirectory path"""
        return self._p

    @p.setter
    def p(self, value):
        # TODO: Verify the 'value' is a directory
        self._p.value = value

    @property
    def d(self):
        """Output Units: 0=meters, 1=centimeters, 2=feet, 3=inches"""
        return self._d

    @d.setter
    def d(self, value):
        # TODO: Verify the 'value' is between 0 and 3
        self._d.value = value

    @property
    def f(self):
        """Specify an alternate Lampdat file."""
        return self._f

    @f.setter
    def f(self, value):
        # TODO: verify 'value' is a valid file
        self._f.value = value

    @property
    def t(self):
        """lamp type from lamp.tab"""
        return self._t

    @t.setter
    def t(self, value):
        self._t.value = value

    @property
    def c(self):
        """RGB color for the lamp as r, g, and b values"""
        return self._c

    @c.setter
    def c(self, value):
        self._c.value = value

    @property
    def u(self):
        """Default lamp color per lookup table. To be used with -f"""
        return self._u

    @u.setter
    def u(self, value):
        self._u.value = value

    @property
    def m(self):
        """multiplier value"""
        return self._m

    @m.setter
    def m(self, value):
        self._m.value = value

