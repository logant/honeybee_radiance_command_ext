"""xform Command."""
import os.path

from honeybee_radiance_command_ext.options.xform import XformOptions
from honeybee_radiance_command._command import Command
import warnings
import honeybee_radiance_command._typing as typing


class Xform(Command):
    """Xform command.

        Xform command doe sstuff...

        Args:
            options: Xform command options. It will be set to Radiance default values
                if unspecified.
            output: Output file (Default: None).
            input: The radiance file to transform (Default: None)

        Properties:
            * options
            * output
            * input
        """
    __slots__ = ('_input',)

    def __init__(self, options=None, output=None, input=None):
        """Initialize Command."""
        Command.__init__(self, output=output)
        if input != None:
            self._input = typing.normpath(input)
        else:
            self._input = input
        self._options = options or XformOptions()

    @property
    def options(self):
        """xform options."""
        return self._options

    @options.setter
    def options(self, value):
        if value is None:
            print('options value is null')
            value = XformOptions()

        if not isinstance(value, XformOptions):
            raise ValueError('Expected XformOptions not {}'.format(type(value)))

        self._options = value

    @property
    def input(self):
        """Input file.

        Get and set inputs files.
        """
        return self._input

    @input.setter
    def input(self, value):
        # ensure input is a valid file path
        # if not os.path.exists(value):
        #    raise ValueError(
        #        'the input file must be a valid, existing radiance file'
        #    )
        self._input = typing.path_checker(value)

    def to_radiance(self, stdin_input=False):
        """Xform in Radiance format.

        Args:
            stdin_input: A boolean that indicates if the input for this command
                comes from stdin. This is for instance the case when you pipe the input
                from another command (default: False).
        """
        self.validate()

        command_parts = [self.command]

        if self.options:
            command_parts.append(self.options.to_radiance())

        command_parts.append('' if stdin_input else self.input)

        cmd = ' '.join(command_parts)

        if self.pipe_to:
            pt = self.pipe_to.to_radiance(stdin_input=True)
            cmd = ' | '.join((cmd, pt))

        elif self.output:
            cmd = ' > '.join((cmd, self.output))

        return ' '.join(cmd.split())

    def validate(self):
        Command.validate(self)
        if not os.path.exists(self._input):
            warnings.warn('xform: no valid input file provided.')
