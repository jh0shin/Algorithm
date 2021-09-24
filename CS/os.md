# Operating System

## Process
- An instance of a running program
- Includes : images, process context
- Process scheduling
- Process switching
    - Running process interruption to another process
    - User mode / Kernel mode
    - Switching overhead
#### System call
- fork() (clone), exec() (run), wait() (sync), exit() (terminate)

## Multithreading
#### Thread
- A sequence of instructions being executed in a program
- Share the process instructions and data
- Thread context : data registers, stack pointer, program counter
- User-level / Kernel-level / combined
- linux pthreads

## Processor scheduling
- Queueing model : server-requests
- Nonpreemptible vs preemptible
- Short-term scheduler (Dispatcher)
- CPU scheduling criteria
    - CPU oriented : utilization, throughput
    - Process oriented : Turnaround, waiting, response time
- CPU-bound vs I/O-bound
#### First-Come First-Served (FCFS) scheduling
- Selection : The process that has been waiting the longest in the waiting queue
- Decision : nonpreemptive
#### Round Robin
- Selection : Same as FCFS
- Decision : interrupt when time slice period (time quantum) has expired
- preemptive
- switching overhead
#### Shortest Job First (SJF) scheduling
- Selection : shortest ***expected*** CPU burst time
- Decision
    - Nonpreemptive : it cannot be preempted
    - Preemptive : compare remaining time of current process and waiting process 
    (Shortest-Remaining-Time-First, SRTF)
- Estimating CPU burst : simple averaging / exponential averaging
#### Multilevel feedback queue scheduling (MLFQ)
- scheduled according to different algorithms
- Each queue has its own scheduling algorithm
- Preemptive scheduling with dynamic priorities
- Process can move between the various queues
#### Fair share scheduling (FSS)


#### UNIX scheduler
- Reward interactive processes over CPU-bound processes
- Real-time scheduling : priority inversion problem -> priority inheritance solution
#### Solaris scheduling
- Priority based, time-sharing, preemptive scheduling
- Four priority classes
- Fully preemptable kernel
#### Window scheduling
- Priority-based, time-sharing, preemptive scheduling
- 32-level priority scheme
#### Linux 2.6 scheduling
- Priority-based, time-sharing, preemptive scheduling
- POSIX.4 compatible

## Process synchronization
- Race condition -> need synchronization mechanisms
- Critical section
    1. Mutual Exclusion
    2. Progress
    3. Bounded waiting (no starvation)
- Low-level synchronization primitive : Locks (spinlock)
- High-level synchronization : semaphore, monitor
#### Locks
- lock() / unlock()
- locks typically spins -> spinlock
#### Semaphre
- A synchronization primitive higher level than locks
- wait(s), signal(s)
- Binary semaphore (= ***mutex***)
    - Guarantees mutually exclusive access to resouce
    - Only one thread / process allowed
    - Initialized to 1
- Counting semaphre
    - Allow threads/processes to enter as long as more units available
    - Initialized to N (number of available units)
#### Deadlock
- Dining-Philosophers problem
#### Critical Region
#### Monitors
#### Message passing

## Deadlock
- A set of blocked processes each holding a resource and waiting to acquire
  a resource held by another process in the set
- Deadlock condition : deadlock can arise if following conditions hold simultaneously
    1. Mutual exclusion
    2. Hold and wait
    3. No preemption
    4. Circular wait
- Prevention : Ensure that one of the four deadlock conditions never occur
- Avoidance : avoid deadlock by run-time checking and allocation of resources

## Memory management
#### Address space
- Physical/logical address space
- Swapping : a process can be swapped temporarily out of memory to backing store
- Simple memory management - no ***virtual memory***
    - Fixed partitioning
    - Dynamic partitioning
- Overlay
#### Buddy system
- Overcome disadvantages of both fixed and dynamic partitioning schemes
#### Paging
- Principles
    - Physical address sapce of a process can be noncontiguous
    - Process's virtual address space is divided into equal sized pages (p, o)
    - Physical memory is divided into equal sized frames (f, o)
    - Pages are mapped to frames
- Associative memory
- Handling large page table -> multi-level paging, hashed page table, inverted page table
#### Segmentation
- A segment is a logical unit such as - code, data, stack
- Segmentation can be viewed as commodity offered to the programmer to organize logically a program into segments and using different kinds of protection
#### Segmentation with paging

## Virtual memory
- Instructions executed by the CPU issue virtual addresses
- Separation of user logical memory from physical memory
- VM enables programs to execute without requiring their entire address space
#### Demand paging
- Bring a page into memory only when it it needed
#### Page replacement
- Need algorithm which will result in minimum number of overall page faults
- Optimal (requires the knowledge of future)
- FIFO - replace the oldest
- LRU(Least Recently Used) - replace the page that has not been used for the longest time
- Clock algorithm
#### Thrashing
- Lack of free frames
- Each process is busy moving pages in and out

## File systems
- File : A named collection of related information that is recorded on secondary storage
- Tree-structed directories
- Acyclic-graph directories (symbolic link)
- inode

## Disk scheduling
- FCFS : fair but inefficient
- SSTF : select request with the minimum seek time. starvation possible
- SCAN (Elevator) : move one direction until the end and reverse
- C-SCAN : more uniform wait time than SCAN
- LOOK
- C-LOOK