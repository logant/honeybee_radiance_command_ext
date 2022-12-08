"""ies2rad Command."""
import os.path

from .options.ies2rad import Ies2radOptions
from honeybee_radiance_command._command import Command
import warnings
import honeybee_radiance_command._typing as typing


class Ies2rad(Command):
    """Ies2rad command.

        Ies2rad converts one or more IES luminaire data files to the equivalent
        RADIANCE scene description.  The light source geometry will  always  be
        centered  at  the  origin aimed in the negative Z direction, with the 0
        degree plane along the X axis.

        Args:
            options: Ies2rad command options. It will be set to Radiance default values
                if unspecified.
            output: Output file (Default: None).
            input: The ies file to convert to Radiance (Default: None)

        Properties:
            * options
            * output
            * input
        """
    __slots__ = ('_input',)

    def __init__(self, options=None, output=None, input=None):
        """Initialize Command."""
        Command.__init__(self)
        self._input = typing.normpath(input)
        self._output = output
        self._options = options or Ies2radOptions()

    @property
    def options(self):
        """Ies2rad options."""
        return self._options

    @options.setter
    def options(self, value):
        if value is None:
            print('options value is null')
            value = Ies2radOptions()

        if not isinstance(value, Ies2radOptions):
            raise ValueError('Expected Ies2radOptions not {}'.format(type(value)))

        self._options = value

    @property
    def input(self):
        """Input files.

        Get and set inputs files.
        """
        return self._input

    @input.setter
    def input(self, value):
        # ensure input is a valid file path
        if not os.path.exists(value):
            raise ValueError(
                'the input file must be a valid, existing IES file'
            )
        self._input = typing.path_checker(value)

    @property
    def output(self):
        """output file.

        Get and set inputs files.
        """
        return self._output

    @output.setter
    def output(self, value):
        # ensure input is a valid file path
        self._output = typing.path_checker(value)

    def to_radiance(self, stdin_input=False):
        """Ies2rad in Radiance format.

        Args:
            stdin_input: A boolean that indicates if the input for this command
                comes from stdin. This is for instance the case when you pipe the input
                from another command (default: False).
        """
        self.validate()

        command_parts = [self.command]

        if self.options:
            command_parts.append(self.options.to_radiance())
        if self.output:
            command_parts.append('-o {0}'.format(self.output))

        command_parts.append(self.input)

        cmd = ' '.join(command_parts)

        return ' '.join(cmd.split())

    def validate(self):
        Command.validate(self)
        if not os.path.exists(self._input):
            warnings.warn('ies2rad: no input IES file provided.')
