#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Answer 1.

def next_greater_element(arr):
    stack = []
    output = [-1] * len(arr)
    
    
    for i in range(len(arr)):
        while stack and arr[i] > arr[stack[-1]]:
            index = stack.pop()
            output[index] = arr[i]
        stack.append(i)
    return output


# In[2]:


n = 4
arr = [1,3,2,4][:n]
result = next_greater_element(arr)
print(' '.join(map(str, result)))


# In[4]:


n = 65
arr =[6,8,0,1,3][:n]
result = next_greater_element(arr)
print(' '.join(map(str, result)))


# In[11]:


#answer 2

def nearest_smaller_elements(arr):
    stack = []
    output = [-1] * len(arr)
    
    for i in range(len(arr)):
        while stack and arr[i] <= arr[stack[-1]]:
            stack.pop()
            
        if stack:
            output[i] = arr[stack[-1]]
            
        stack.append(i)
        
    return output


# In[12]:


n = 3
arr = [1,6,2][:n]
result = nearest_smaller_elements(arr)
print(' '.join(map(str, result)))


# In[14]:


n = 6
arr =[1, 5, 0, 3, 4, 5][:n]
result = nearest_smaller_elements(arr)
print(' '.join(map(str, result)))


# In[19]:


#Answer 3.

class Stack:
    def __init__(self):
        self.q1 = []
        self.q2 = []

    def push(self, value):
        self.q1.append(value)

    def pop(self):
        if not self.q1:
            return None

        while len(self.q1) > 1:
            self.q2.append(self.q1.pop(0))

        popped = self.q1.pop(0)

        self.q1, self.q2 = self.q2, self.q1

        return popped

    def top(self):
        if not self.q1:
            return None

        return self.q1[-1]

    def is_empty(self):
        return len(self.q1) == 0


# In[20]:


stack = Stack()
stack.push(2)
stack.push(3)
print(stack.pop()) 
stack.push(4)
print(stack.pop()) 


# In[22]:


stack = Stack()
stack.push(2)
print(stack.pop())
print(stack.pop())
stack.push(3)


# In[23]:


#Answer 4.

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            return None
        return self.items.pop()

    def reverse_stack(self):
        if self.is_empty() or len(self.items) == 1:
            return

        top_element = self.pop()

        self.reverse_stack()

        self.insert_at_bottom(top_element)

    def insert_at_bottom(self, item):
        if self.is_empty():
            self.push(item)
        else:
            top_element = self.pop()
            self.insert_at_bottom(item)
            self.push(top_element)


# In[24]:


stack = Stack()
stack.push(3)
stack.push(2)
stack.push(1)
stack.push(7)
stack.push(6)


print("Original Stack:", stack.items)
stack.reverse_stack()
print("Reversed Stack:", stack.items)


# In[25]:


stack = Stack()
stack.push(4)
stack.push(3)
stack.push(9)
stack.push(6)

print("Original Stack:", stack.items)
stack.reverse_stack()
print("Reversed Stack:", stack.items)


# In[1]:


#Answer 5.


def reverse_string(String):
    stack = list(string)
    
    stack.reverse()

    reversed_string = ''.join(stack)
    
    return reversed_string


# In[4]:


string ="GeeksforGeeks"
reversed_string = reverse_string(string)
print("Original String:", string)
print("Reversed String:", reversed_string)


# In[25]:


#answer 6.

def evaluate(expressions):
    stack = []
    for char in expressions:
        if char.isdigit():
            stack.append(int(char))
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            if char == '+':
                result = operand1 + operand2
            elif char == '-':
                result = operand1 - operand2
            elif char == '*':
                result = operand1 * operand2
            elif char == '/':
                result = operand1 / operand2
            stack.append(result)
    return stack.pop()


# In[26]:


expressions = "231*+9-"
result = evaluate(expressions)
print(result)


# In[27]:


expressions = "123+*8-"
result = evaluate(expressions)
print(result)


# In[19]:


#Answer 7.

class Minstack:
    def __init__(self):
        self.stack = []
        self.min_stack = []
        
    def push(self, val):
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1][0]:
            self.min_stack.append((val, len(self.stack) -1))
            
    def pop(self):
        if self.stack:
            popped = self.stack.pop()
            if self.min_stack and self.min_stack[-1][1] == len(self.stack):
                self.min_stack.pop()
                
    def top(self):
        if self.stack:
            return self.min_stack[-1]
        
    def getMin(self):
        if self.min_stack:
            return self.min_stack[-1][0]


# In[20]:


stack = Minstack()
stack.push(-2)
stack.push(0)
stack.push(-3)
print(stack.getMin())  
stack.pop()
print(stack.top())  
print(stack.getMin()) 


# In[25]:


#Answer 8.

def trap(height):
    n = len(height)
    left = 0
    right = n -1
    left_max = 0
    right_max = 0
    water = 0
    
    while left < right:
        if height[left] < height[right]:
            if height[left] > left_max:
                left_max = height[left]
            else:
                water += left_max - height[left]
            left += 1
        else:
            if height[right] > right_max:
                right_max = height[right]
            else:
                water += right_max - height[right]
            right -= 1
            
    return water


# In[26]:


height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
trapped_water = trap(height)
print(trapped_water)


# In[ ]:




