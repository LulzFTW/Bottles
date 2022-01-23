from typing import NewType

from bottles.utils import UtilsLogger # pyright: reportMissingImports=false
from bottles.backend.wine.wineprogram import WineProgram

logging = UtilsLogger()

# Define custom types for better understanding of the code
BottleConfig = NewType('BottleConfig', dict)


class CMD(WineProgram):
    program = "WINE Command Line"
    command = "cmd"

    def run_batch(
        self, 
        batch: str, 
        terminal: bool = True, 
        args: str = "",
        environment: dict = {},
        cwd: str = None
    ):
        args = f"/c {batch} {args}"
        
        self.launch(
            args=args,
            comunicate=True,
            terminal=terminal,
            environment=environment,
            cwd=cwd
        )