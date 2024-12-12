#this class for create memory blocks
class MemoryBlock:
    def __init__(self, size):
        self.size = size
        self.is_free = True  #assign true/allocate block when it creating

#this class for allocate and deallocate value for memory block
class NextFitAllocator:
    def __init__(self, memory_sizes):
        self.memory_blocks = [MemoryBlock(size) for size in memory_sizes]
        self.last_allocated_index = -1  # Start before the first block

    def allocate(self, request_size):
        num_blocks = len(self.memory_blocks)
        start_index = (self.last_allocated_index + 1) % num_blocks

        # Start searching from the next block
        for i in range(num_blocks):
            index = (start_index + i) % num_blocks
            block = self.memory_blocks[index]
            
            if block.is_free and block.size >= request_size:
                # Allocate this block
                block.is_free = False
                self.last_allocated_index = index
                print(f"Allocated {request_size} units to block {index} (size {block.size}).")
                return index

        # If no suitable block is found
        print(f"Failed to allocate {request_size} units: no suitable block found.")
        return -1

    #deallocate block
    def deallocate(self, block_index):
        if 0 <= block_index < len(self.memory_blocks):
            block = self.memory_blocks[block_index]
            if not block.is_free:
                block.is_free = True
                print(f"Deallocated block {block_index} (size {block.size}).")
            else:
                print(f"Block {block_index} is already free.")
        else:
            print(f"Invalid block index {block_index}.")

    #Display all block,size and status
    def display_memory(self):
        print("\nMemory Blocks Status:")
        for i, block in enumerate(self.memory_blocks):
            status = "Free" if block.is_free else "Allocated"
            print(f"Block {i}: Size={block.size}, Status={status}")
        print()

# Main
if __name__ == "__main__":
    # Initialize memory blocks (sizes in units)
    memory_sizes = [50, 70, 30, 100, 60]
    allocator = NextFitAllocator(memory_sizes)

    allocator.display_memory()
    
    # Allocate memory
    allocator.allocate(60)
    allocator.allocate(40)
    allocator.allocate(20)
    
    allocator.display_memory()

    # Deallocate memory
    allocator.deallocate(1)
    allocator.display_memory()

    # Attempt to allocate again
    allocator.allocate(90)
    allocator.display_memory()
