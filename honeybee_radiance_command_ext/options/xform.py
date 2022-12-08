"""Xform parameters."""
from honeybee_radiance_command.options.optionbase import OptionCollection, NumericOption, IntegerOption,\
    BoolOption, TupleOption


class XformOptions(OptionCollection):
    """
    xform [-s scalar] [-t xcoord ycoord zcoord] [-rx angle] [-ry angle] [-rz angle] [-mx] [-my] [-mz] [-i qty] input_file > output_file

    Also see: https://floyd.lbl.gov/radiance/man_html/xform.1.html
    """

    __slots__ = ('_t', '_rx', '_ry', '_rz', '_s', '_mx', '_my', '_mz', '_i')

    def __init__(self):
        """Xform command options."""
        OptionCollection.__init__(self)
        self._t = TupleOption('t', 'translate the scene along vector x y z', None, 3, float)
        self._rx = NumericOption('rx', 'rotate the scene about the x axis (degrees)', None)
        self._ry = NumericOption('ry', 'rotate the scene about the y axis (degrees)', None)
        self._rz = NumericOption('rz', 'rotate the scene about the z axis (degrees)', None)
        self._s = NumericOption('s', 'scale factor', value=1.0)
        self._mx = BoolOption('mx', 'mirror about the yz plane', None)
        self._my = BoolOption('my', 'mirror about the xz plane', None)
        self._mz = BoolOption('mz', 'mirror about the xy plane', None)
        self._i = IntegerOption('i', 'repeat the following transformations n times.', None)
        self._on_setattr_check = True

    def _on_setattr(self):
        """This method executes after setting each new attribute.

        Use this method to add checks that are necessary for OptionCollection. For
        instance in rtrace option collection -ti and -te are exclusive. You can include a
        check to ensure this is always correct.
        """

    @property
    def t(self):
        """specify the translation vector"""
        return self._t

    @t.setter
    def t(self, value):
        self._t.value = value

    @property
    def rx(self):
        """specify the x axis rotation in degrees"""
        return self._rx

    @rx.setter
    def rx(self, value):
        self._rx.value = value

    @property
    def ry(self):
        """specify the y axis rotation in degrees"""
        return self._ry

    @ry.setter
    def ry(self, value):
        self._ry.value = value

    @property
    def rz(self):
        """specify the z axis rotation in degrees"""
        return self._rz

    @rz.setter
    def rz(self, value):
        self._rz.value = value

    @property
    def s(self):
        """Specify the scale (1.0 is 100%)"""
        return self._s

    @s.setter
    def s(self, value):
        self._s.value = value

    @property
    def mx(self):
        """mirror across X axis"""
        return self._mx

    @mx.setter
    def mx(self, value):
        self._mx.value = value

    @property
    def my(self):
        """Mirror across Y axis"""
        return self._my

    @my.setter
    def my(self, value):
        self._my.value = value

    @property
    def mz(self):
        """Mirror across Z axis"""
        return self._mz

    @mz.setter
    def mz(self, value):
        self._mz.value = value

    @property
    def i(self):
        """specify iteration quantity"""
        return self._i

    @i.setter
    def i(self, value):
        self._i.value = value
