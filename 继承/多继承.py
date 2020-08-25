#__author__:"Ming Luo"
#date:2020/8/25

# 当一个类继承自多个类的时候，那么这个子类会同时拥有这多个类的属性和方法


class A:
    def test(self):
        print("A test")


class B:
    def demo(self):
        print("B demo")


class C(A, B):
    pass


c = C()
c.test()
c.demo()


# ！！ 当这多个类拥有相同的属性或者方法的时候尽量不要用多继承，这样会使代码的可读性变差
class A:
    def test(self):
        print("A test")

    def demo(self):
        print("A demo")


class B:
    def test(self):
        print("B test")

    def demo(self):
        print("B demo")


# class C(A, B):
#     pass


class C(B, A):
    pass


c = C()
c.test()
c.demo()

