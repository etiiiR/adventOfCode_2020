from dataclasses import dataclass, field
from typing import List


@dataclass
class Game_Accumulator:
    '''Class for keeping track of an item in inventory.

    Constructor arguments:
    :param name: name of the item
    :param unit_price: price in USD per unit of the item
    :param quantity_on_hand: number of units currently available
    '''
    codes_to_process: List = field(default_factory=list)
    path: str = ''
    _alerady_read: List = field(default_factory=list)
    _state: int = 0
    _line: int = 0
    _jump: str = "jmp"
    _accumulate: str = "acc"
    _init: str = "acc"
    
    
    @property
    def state(self) -> int:
        return self._state
    
    @property
    def jump(self) -> str:
        return self._jump
    
    
    def set_steps(self):
        with open(self.path) as f:
            read_data = f.read()
        lst_data = read_data.splitlines()
        self.codes_to_process = [i.split(' ') for i in lst_data]
        return True
    
    
    def run_steps(self):
        while self._line not in self._alerady_read:
            self._alerady_read.append(self._line)
            if(self.codes_to_process[self._line][0] == self._init):
                pass
            elif(self.codes_to_process[self._line][0] == self._jump):
                self._line += int(self.codes_to_process[self._line][1])
                continue
            elif(self.codes_to_process[self._line][0] == self._accumulate):
                self._state += int(self.codes_to_process[self._line][1])
            self._line += 1
        return True


if __name__ == "__main__":
    accumulator1 = Game_Accumulator()
    accumulator1.path="./text1.txt"
    
    accumulator2 = Game_Accumulator()
    accumulator2.path="./text2.txt"
    
    accumulator3 = Game_Accumulator(path="./text3.txt")
    
    accumulator1.set_steps()
    accumulator1.run_steps()
    
    accumulator2.set_steps()
    accumulator2.run_steps()
    
    accumulator3.set_steps()
    accumulator3.run_steps()
    
    print(accumulator1.state)
    print(accumulator2.state)
    print(accumulator3.state)
