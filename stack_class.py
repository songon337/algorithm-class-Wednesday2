# stack_class.py
#########################################################################################
#array로 구현한 stack 클래스
# 메소드들: is_empty,is_full,push,pop,peek,size
#########################################################################################

class ArrayStack:
    def __init__(self, capacity):
        self.capcity = capacity
        self.array = [None] * capacity
        self.top = -1

    def is_empty(self):
        return self.top == -1
    
    def is_full(self):
        return self.top == self.capcity - 1
    

    def push(self, item):
        if not self.is_full():
            self.top += 1
            self.array[self.top] = item
            print(f"PUSH: {item!r} -> stack is now {self.array[:self.top + 1]}")
        else:
            raise OverflowError("Stack Overflow") # pass , exit(1)
        
    def pop(self):
        if not self.is_empty():
            item = self.array[self.top]
            self.array[self.top] = None
            self.top -=1
            print(f"POP: {item!r} -> stack = {self.array[self.top + 1]}")
            return item
        else:
            raise IndexError("Stack underflow")

    def peek(self):
        if not self.is_empty():
            return self.array[self.top]
        return None
    
    def size(self):
        return self.top + 1
    
    # 스택 클래스를 이용한 문자열 거꾸로 뒤집어 출력하기
    def reverse_string(statement):
        print("\n[1] PUSH 단계 -----------------------")
        st = ArrayStack(len(statement))
        for ch in statement:
            st.push(ch)

        print("\n[2] POP단계 -----------------------")
        out = []
        while not st.is_empty():
            out.append(st.pop())

        result = ''.join(out)
        print(f"\n[3] 최종 결과 : {result}")
        return result

def test_reverse():
    tests = ["토마토","안녕하세요 반갑습니다.", "123456"]

    for s in tests:
         got = reverse_string(s)

    if __name__ =="__main__":
          test_reverse()