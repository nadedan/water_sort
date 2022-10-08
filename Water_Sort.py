from __future__ import annotations
from collections import deque
from typing import Union

class Block():
    def __init__(self,
                 color:str
                ):
        self.color = color

    @property
    def height(self) -> int:
        return 1



class Stack():
    '''
    Stack Class

        An abstraction of the tube in the water sort puzzle. A stack has a size, which determines how many
        blocks of water that it can hold. The blocks of water are kept in a stack in a FILO queue.

        While the stack of blocks is internally handled as a deque object, the init_state input
        is a simple list, where the 0th element is the bottom of the stack.
    '''
    def __init__(self,
                 size:int=None,
                 init_state:list(Block)=None,
                ):
        if size is None:
            # default size is 4
            size = 4

        if init_state is None:
            # Create an empty list of for the state
            init_state = []

        # Store the size
        self.size = size
        # Create our stack of blocks
        self.blocks = deque(maxlen=self.size)

        # Put the starting blocks in the stack
        for this_block in init_state:
            self.blocks.append(this_block)

    @property
    def height(self) -> int:
        return len(self.blocks)

    @property
    def top_block(self) -> Block:
        return self.block_from_top(0)

    @property
    def block_from_top(self, dist_from_top:int) -> Block:
        '''
        Easy way to look down the stack
        '''
        if dist_from_top >= self.height:
            return None
        else:
            return self.blocks[len(self.blocks)-1 - dist_from_top]

    @property
    def top_stack(self) -> Stack:
        '''
        Start at the top of the stack.
        Go down until you hit a different color.
        Return the stack from there to the top.
        '''
        if self.height == 0:
            return None

        ret_stack = Stack(size=self.size)
        this_block = self.top_block
        ret_stack.add(self.top_block)

        while ret_stack.height < self.height:
            this_block = self.block_from_top(ret_stack.height)

            if this_block.color == ret_stack.top_block.color:
                ret_stack.add(this_block)
            else:
                break

        return ret_stack

    def add(self, new_top:Union[Block, Stack]):
        '''
        Put more blocks on top of the stack.
        '''

        # Make sure we have room for the st
        if self.height + new_top.height <= self.size:
            # We have room, so add the blocks
            # Check to see if we are adding a Block or Stack
            if isinstance(new_top, Block):
                # We are adding a single block
                self.blocks.append(new_top)

            if isinstance(new_top, Stack):
                # We are adding a stack of blocks
                for this_block in new_top.blocks:
                    self.blocks.append(this_block)
        else:
            # Not enough room. Raise an exception
            raise

    def remove(self, count:int):
        '''
        Removes count blocks from the top of the Stack
        '''
        try:
            for i in range(count):
                _ = self.blocks.pop()

        except IndexError:
            # We exhausted the list of blocks
            pass

pass
