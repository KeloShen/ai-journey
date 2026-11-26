---
title: Learning Python & algorithms with an AI tutor (81 Q&As, 65 logged mistakes)
title_zh: 和 AI 导师一起学 Python 与算法（81 条问答、65 条错题）
title_de: Python & Algorithmen mit einem KI-Tutor lernen (81 Fragen, 65 Fehler)
date: 2026-11-23
tool: Claude
topics: [Python, Data structures & algorithms, LeetCode, OOP]
---

> **About this log** · From 2 to 23 November 2026 I studied Python and data structures & algorithms (LeetCode) with an AI tutor. Instead of asking for answers, I asked "why", pasted my own buggy code, and had the AI keep a structured notebook: every question with where I got stuck and how it was explained, a mistake log, and a running list of my weak spots. The notes below are that notebook, unedited (in Chinese).

# Programming 学习笔记

## 目录 / 课程地图

| 练习 | 主题 | 状态 |
|---|---|---|
| Ex1 | – | 未整理 |
| Ex2 | – | 未整理 |
| Ex3 | – | 未整理 |
| Ex4 | – | 未整理 |
| Ex5 | – | 未整理 |
| 课外 / OOP | `self`、bound method、赋值 = 移动名字标签；继承、`super()`、自定义异常、`try`/`except` 的执行流程；PEP 8 命名规范；类变量 / 实例变量 / 局部变量；方法 vs 嵌套函数的 `self`、`@staticmethod`；共享变量放在哪（实例 / 类 / 树）；类变量的读写与遮蔽、LEGB 跳过 class | 问答 7 条，错题 7 条 |
| Python 语法 | 解包（`*rest`、`enumerate`、`zip`、`f(*args)`）；字典（`fromkeys` 的坑、插入顺序、读/写规则、`get`、`defaultdict`、`Counter`）；`for` 循环变量每轮被重新赋值；`print()` 的底层流程；`*` / `**` 的打包与解包（接收的一边打包、给出的一边解包）；`deque` / `list` / `queue.Queue`；哈希表的遍历顺序；`set` 也是哈希表、查找平均 O(1)（hash：key → 下标）；`Optional[X]` 与类型注解；`not x` vs `x is not None`（真值 vs None）；浅拷贝 vs 深拷贝（新容器 + 共享元素）、赋值 = 换地址、列表 `+=` 原地修改；for 里解包 `dx, dy`；`sort` 的 `key` 是函数、`lambda`、`key=len`、元组 key 多级排序；`reverse=True` vs `list.reverse()`（原地方法返回 None）；hash set vs hash map、冲突处理（开放寻址 / 拉链法） | 问答 16 条，错题 8 条 |
| 刷题 / LeetCode | 前缀和：1314（二维，待提交）、724；差分数组 370；字符串 151；模拟 54 螺旋矩阵；单调栈（下一个更大元素）；「代入法」合并特殊情况；快慢指针 26；中心扩展 5；滑动窗口 76、567（及均摊复杂度）；双指针 15 三数之和、18 四数之和（nSum 递归）；42 接雨水（暴力 → 预处理最大值）；二分查找（左右边界、越界、插入位置、`mid ± 1`）；1011 二分答案；239 单调队列；128 最长连续序列（哈希）；链表：141 快慢指针、21 虚拟头节点（哨兵）、23 堆合并 K 个链表（元组比较、`__lt__`）、160 相交链表、206 递归反转；二叉树：94 / 145 遍历、102 层序、111 最小深度、543 直径、高度平衡树 O(log N)；快速排序 partition；回溯框架（全排列）；BST：230 用 `size` 求排名、98 用 `(min, max)` 验证；98 遍历 vs 分解（前序传参 / 后序返回 `(ok, min, max)` / 中序 + prev）、哨兵 `inf`、DP vs 分治、末尾 `return` 的作用；700 搜索、BST 最小节点、450 删除；96 不同的 BST（乘法原理 + 备忘录 → DP）；图：邻接表 `Edge`、`visited` vs `onPath` 判环与剪枝、797 所有路径；Union-Find：路径压缩的摊还分析、130 被围绕的区域、261 以图判树（无环 + 连通）、1135 / 1584 Kruskal；654 最大二叉树；LCA 前置 find（转交孩子的结果）；106 中序 + 后序、889 前序 + 后序建树（区间与 base case）；70 爬楼梯（备忘录）；354 信封（元组 key + LIS）；二分边界：闭区间 vs 左闭右开、循环不变量推左 / 右边界 | 问答 58 条，错题 51 条 |

**薄弱点**
- 赋值的语义：容易把 `b = a` 理解成「b 跟着名字 a 走」，或者以为它是浅拷贝；以为 `cur = dq[0]` 会跟着队头自动变、`mid` 写在 while 外面（每轮要变的量必须写在循环里）；以为浅拷贝存的是原列表的地址（浅拷贝 = 新容器 + 共享元素，`=` 换地址、方法改对象）（见错题本 #1、#2、#3、#41、#51、#64）
- `list * n` 复制的是引用，不是对象（见错题本 #3）
- 边界 off-by-one：「最后一个下标」和「`range` 的开区间终点」容易混用；切片 / 区间把根也包进去、左子树个数多 1、闭区间里「空」和「单元素」分不清（见错题本 #4、#56、#59、#60）
- 学过的规则，写代码时没用上：刚记完 #3，在 1314 里又写了两次 `[[0]*m]*n` / `[[0]*n]*m`，第二次自己没看出来（**最高优先级回炉**）；类里的辅助方法调用时没加 `self.`，定义时也漏了 `self`（见错题本 #6）
- `except` 的匹配顺序：只有第一个匹配的分支会执行（见错题本 #5）
- 方法里不带前缀的名字一律是**局部变量**，不是类变量（见错题本 #7）
- 会不自觉地用别的语言的写法（`++`）（见错题本 #8）
- 坐标约定：数学里「x = 横坐标」和二维列表 `[行][列]` 容易混用（见错题本 #10）
- 函数最后忘了 `return`（见错题本 #9）
- 指针停在哪里：`while` 退出时指针在区间里还是外面、要不要再 `±1`、移动写在分支里还是外面（见错题本 #12、#13，问答 Q9、Q10）
- 复制粘贴的条件没核对 / 边界条件方向写反，循环没有进展 → 死循环、超时、内存超限（见错题本 #11、#20）
- 方法调用：漏 `self.`、漏 `()`、主语搞错（`pop(x)`、`list.join`）、漏模块前缀 `heapq.`、递归调成了入口函数（见错题本 #6、#16、#18、#35、#43、#63）——同类错误已经出现 6 次，其中「递归调入口函数」**2 次**；调用时漏参数（#61）
- `self` 和作用域：嵌套函数不写 `self`；方法里看不到类体变量（LEGB 跳过 class），类变量要 `self.` / `类名.`；可变的类变量（`res = []`、`value_to_index = {}`）会被所有实例共享（见错题本 #39、#40、#59）
- 类型注解写成圆括号 `Optional(TreeNode)`，应为 `Optional[TreeNode]`——**已出现 7 次**（见错题本 #16、#39、#43、#46、#48、#49、#59），而且同一份代码里另一行写对了；889（#61）终于写对了 ✅，继续保持；别用 `min` / `max` 当变量名（见 #46）
- 两个「看起来一样」的量混用：`len(need)` vs `len(s1)`、`0` / `None` / `[]`、`[1,2,3]` vs `([1,2,3],)`、`x` vs `'x'`（见错题本 #14、#22、#29、#30）
- 计数器 / 状态的更新时机：只在刚好跨过界限时变化（见错题本 #21）
- 去重 / 跳过的时机：先处理再跳、和前一个比还是和后一个比（见错题本 #13、#23、#25）
- 「碰巧对」：参数没用上、示例全过、重构时丢了一行——要自己构造极端用例：只有一个孩子的节点、树很矮时 parent 碰巧是根、小 n 不走到出错分支（见错题本 #24、#26、#27、#54、#60、#63）
- **先检查，再更新**：指针只在「这一步确实成功了」之后移动（见错题本 #12、#25、#31）
- deque 的两头：`[0]`/`popleft` 是左，`[-1]`/`pop` 是右；检查和删除要是同一头（见错题本 #33）
- None 检查：访问 `.next` / `.val` 之前先确认不是 None，访问几层检查几层；容器空 ≠ 元素空；`not head` ⇔ `head is None`（见错题本 #34、#35、#36）
- 「做了要撤销」：共享状态进入 +1、离开 −1，**每个出口**都要对称；能用参数传就用参数（见错题本 #42，问答 Q48、Q51、Q53）
- 量是「相对于谁」的：局部排名 vs 全局排名、i 和 j 停止条件相反（见错题本 #44、#45）
- 带返回值的递归：每条路径都要按定义 `return`；互斥情况用 `if / elif / else`；调用自己后要接住返回值（`root.right = ...`）；base case 也要带值（`return x` 不是 `return`）；中间节点要把孩子的结果转交上去（见错题本 #48、#49、#55、#58，问答 Q57、Q74）
- base case 怎么写：先问「下面的代码依赖哪些假设、什么时候不成立」，而不是「什么时候会崩」；每次递归规模必须严格变小（见错题本 #56、#61、#62）
- 原地修改的方法（`sort`、`reverse`、`append`）返回 None，别用它们的返回值（见错题本 #53）
- 看不懂循环时别逐轮模拟，先找**循环不变量**（每轮结束一定成立的话）；二分左边界学过两次才真正掌握（Q26 → Q80），用不变量自己推出了右边界 ✅（见错题本 #65）
- 维度别混：前 / 中 / 后序（何时做事）、DFS / BFS（访问顺序）、遍历 / 分解（答案怎么来）是三件事（见错题本 #47，问答 Q54、Q57）
- 条件重叠时注意判断顺序：先查 `onPath` 再查 `visited`（见错题本 #52）

---

## 一、学习笔记（按练习）

### Ex1
### Ex2
### Ex3
### Ex4
### Ex5

---

## 二、问答记录

### 课外 / OOP

#### Q1 · `self` 是什么？是怎么传进去的？bound method 又是什么？
- **时间**：2026-11-02 09:27
- **原始问题**：读到一段教程，里面说 *"when you instantiate a new object in Python, self is automatically passed through as the first argument"*。想知道 `self` 是什么、在 Python 里是怎么定义的、怎么传进去的、传进去的是什么信息，有没有直观的源码。追问：bound method 是什么？
- **卡点**：调用时从来没写过 `self`，那它是从哪来的？
- **讲解过程**：
  1. **为什么需要 `self`**：一个类只有**一个** `raise_pay` 函数，但对象有很多（`a`、`b`）。函数要靠 `self` 知道该改哪个对象。`self` 不是关键字，只是第一个位置参数（叫 `emp` 也可以）。
  2. **方法调用就是语法糖**：`a.raise_pay(0.1)` ≡ `Employee.raise_pay(a, 0.1)`。
  3. **bound method = 函数 + 对象粘在一起**。访问 `a.raise_pay` 时，函数的 `__get__`（描述符协议）会造出一个 bound method：
     ```python
     m = a.raise_pay
     m.__func__      # Employee.raise_pay（类里那个普通函数）
     m.__self__ is a # True（粘进去的对象）
     m(0.1)          # → m.__func__(m.__self__, 0.1)
     ```
     简化版的纯 Python 实现：
     ```python
     class BoundMethod:
         def __init__(self, func, obj):
             self.__func__, self.__self__ = func, obj
         def __call__(self, *args, **kw):
             return self.__func__(self.__self__, *args, **kw)  # self 就是在这里塞进去的
     ```
     类比：`Employee.raise_pay` 是一张空白表格（「给 ____ 涨工资」），`a.raise_pay` 是已经填好「Alice」的表格。
  4. **`__init__` 里的 `self`**：`Employee("Alice", 5000)` 走的是 `type.__call__`：
     ```python
     obj = cls.__new__(cls)          # 先造一个空对象
     obj.__init__("Alice", 5000)     # → Employee.__init__(obj, ...)
     return obj
     ```
     所以 `__init__` 里的 `self` 就是刚造出来、还空着的那个对象（`id(self) == id(e)`）。`__init__` 只负责往里填属性，返回 `None`。
  5. **CPython 源码位置**：`Objects/typeobject.c` → `type_call`；`Objects/funcobject.c` → `func_descr_get`（返回 `PyMethod_New(func, obj)`）；`Objects/classobject.c` → `method_vectorcall`。
  6. 每次写 `a.raise_pay` 都会新造一个 bound method：`a.raise_pay is a.raise_pay` → `False`，但 `==` → `True`。
- **结论**：`self` 就是调用方法的那个对象；`a.f(x)` 是 `type(a).f(a, x)` 的简写。bound method 在被创建的那一刻就把**对象**（不是变量名）粘了进去。
- **关联**：OOP / 类与方法；描述符协议；→ 错题本 #1、#2

#### Q3 · 自定义异常：继承、`super().__init__`、`try`/`except` 的执行流程
- **时间**：2026-11-02 10:36
- **原始问题**：看教程里的这段代码：
  ```python
  class CustomError(Exception):
      def __init__(self, message):
          super().__init__(message)

  custom_exception = CustomError("This is a custom error message")
  try:
      raise custom_exception
  except CustomError as ce:
      print(f"Caught a custom exception: {ce}")
  ```
  问：这是继承吗？父类是 `Exception` 吗？`__init__` 里为什么要调用 `super().__init__`？`try`/`except` 的执行流程是怎样的？
- **卡点**：不清楚 `super()` 是干什么的；不清楚 `except` 是怎么匹配的、匹配顺序是怎样的。
- **讲解过程**：
  1. **继承**：`class CustomError(Exception)` → `CustomError` 是子类，`Exception` 是父类（基类 / 超类）。为什么要继承 `Exception`：
     - `raise` 只接受 `BaseException` 子类的对象（`raise 42` → `TypeError`）；
     - `except X` 是用 `isinstance(err, X)` 来匹配的。
     继承之后，`raise` 和 `except` 都认得它，还能白拿父类的功能（保存 message、打印、traceback）。
  2. **`super().__init__(message)`**：
     - 子类自己定义了 `__init__` 就会**覆盖**父类的，父类的 `__init__` 不会再自动执行，它负责的初始化（比如异常要把 message 存进 `self.args`）就被跳过了。
     - `super()` = 「父类，并且绑定在同一个 `self` 上」。`super().__init__(message)` ≈ `Exception.__init__(self, message)`，和 bound method 是同一个道理。
     - 套路：**先让父类做它那部分，再加自己的东西。**
       ```python
       class InsufficientFundsError(Exception):
           def __init__(self, balance, amount):
               super().__init__(f"balance {balance} < {amount}")
               self.balance, self.amount = balance, amount
       ```
     - 实话说：教程里那个 `__init__` 什么都没加，可以整个删掉，写成 `class CustomError(Exception): pass`，行为一样。
  3. **`try`/`except` 的执行流程**：
     1. 开始执行 `try` 块；
     2. `raise` 抛出异常对象，那一行**立刻停下**；
     3. `try` 块里剩下的代码全部**跳过**；
     4. **从上到下**检查每个 `except`：`isinstance(exc, X)` 成立吗？
     5. **第一个**匹配的分支执行，`as ce` 把名字 `ce` 挂到**同一个**异常对象上（又是名字标签）；`{ce}` 会调用 `str(ce)`，得到 message；
     6. 之后从整个 `try` 语句**后面**继续执行；
     7. 一个都没匹配上 → 异常往外抛给调用者，再给调用者的调用者……一直没人接住 → 程序终止并打印 traceback（例如 1314 里的 `NameError`：`matrixBlockSum` → `_driver` → `<module>`）。
     - `else:` 只在没发生异常时执行；`finally:` 无论如何都会执行（之后再展开）。
  4. 追问：改成 `except Exception as e:` 还能接住吗？→ 我答对了：能，因为 `CustomError` **是一种** `Exception`。副作用：`except Exception` 范围太大，会把真正的 bug（比如 `NameError`）也吞掉。
- **结论**：继承 = 「是一种」的关系；子类覆盖了 `__init__` 就要调用 `super().__init__(...)`（≈ `Parent.__init__(self, ...)`）；`except` 从上到下用 `isinstance` 匹配，**只执行第一个匹配的分支**，所以要**先写具体的、后写宽泛的**。
- **关联**：OOP / 继承、`super()`；异常处理；bound method（Q1）；→ 错题本 #5

#### Q5 · PEP 8 命名规范
- **时间**：2026-11-02 13:37
- **原始问题**：读 https://peps.python.org/pep-0008/#naming-conventions，总结一下：变量、method、function、class 的名字应该怎么写？追问：所以一般不要用 CamelCase，要用下划线？
- **卡点**：不确定 CamelCase 能不能用、该用在哪里。
- **讲解过程**：
  | 对象 | 风格 | 例子 |
  |---|---|---|
  | 变量 | `lower_case_with_underscores` | `row_start`、`total` |
  | 函数 | `lower_case_with_underscores` | `block_sum()` |
  | 方法 | 同函数；实例方法第一个参数是 `self`，类方法第一个参数是 `cls` | `raise_pay(self)` |
  | 类 | `CapWords`；缩写全部大写 | `Solution`、`HTTPServerError` |
  | 异常 | 类的规则 + 以 `Error` 结尾 | `CustomError` |
  | 常量（模块级） | `UPPER_CASE_WITH_UNDERSCORES` | `MAX_SIZE` |
  | 模块 / 包 | 短、全小写；模块名可以带下划线，包名尽量不带 | `my_utils` / `mypackage` |
  | 类型变量 | 短的 CapWords | `T`、`AnyStr` |
  - 下划线形式：`_name` 内部使用 / 非公开（`from M import *` 会跳过）；`name_` 避开关键字冲突（`class_`）；`__name` 名字改写；`__name__` 留给 Python，**不要自己发明**。
  - 不要用 `l`、`O`、`I` 做单字母变量名（和 `1`、`0` 看起来很像）。
  - 拿不准是否公开时，先用 `_name`，以后改成公开比反过来容易。
  - **CamelCase 不是禁用的，它只用来给类命名**；PEP 8 要避免的是 **mixedCase**（首字母小写，比如 `matrixBlockSum`）用在函数 / 变量上。只有在必须和已有代码保持一致时才用（比如 LeetCode 规定的方法名）。
  - 好处：看名字就知道是什么。`Employee(...)` 首字母大写 → 类；`block_sum(...)` → 函数。
- **小测**：`class bank_account` ❌ → `BankAccount`；`def getUserName()` ❌ → `get_user_name`；`user_count = 0` ✅；`class HTTPRequest` ✅ → 我答 3、4，全对 ✅
- **结论**：首字母大写 → 类；小写 + 下划线 → 其他所有东西；全大写 → 常量；`__xxx__` 不要自己发明。
- **关联**：Q4（`__sum__` → `_block_sum`）

#### Q6 · 方法里不带 `self.` 的变量是类变量吗？
- **时间**：2026-11-02 13:37
- **原始问题**：在 class 的 `__init__` 构造函数中，如果变量名前面没有 `self`，那就说明这个是 class 的变量而不是 instance 的变量吗？追问：有没有特殊的表示（关键字）来表示类变量？
- **卡点**：以为「方法里没有 `self.`」= 类变量。
- **讲解过程**：
  1. **三种变量**：
     ```python
     class Employee:
         raise_rate = 1.04          # ① 类变量：写在 class 里、方法外面
         def __init__(self, name, pay):
             self.name = name       # ② 实例变量：挂在这个对象上
             bonus = pay * 0.1      # ③ 局部变量：__init__ 返回后就没了
             self.pay = pay + bonus
     ```
     | | 定义在哪里 | 属于谁 | 生命周期 | 怎么访问 |
     |---|---|---|---|---|
     | ① 类变量 | class 里、方法外面 | 类（所有对象共享） | 和类一样长 | `Employee.raise_rate` / `self.raise_rate`（只读） |
     | ② 实例变量 | 方法里写 `self.x = ...` | 某一个对象 | 和对象一样长 | `self.name`、`e.name` |
     | ③ 局部变量 | 方法里写 `x = ...` | 这一次函数调用 | 到方法返回为止 | 只能在方法内部用 |
     验证：`e.__dict__` → `{'name': ..., 'pay': ...}`，里面没有 `bonus`。
  2. **`count = count + 1` 为什么会报 `UnboundLocalError`**：Python 在执行前先扫一遍方法体，只要看到对 `count` 的赋值，就认定 `count` 在**整个方法里**都是局部变量 → 算右边时要读这个局部 `count`，但它还没绑定任何值 → 报错。即使没有这个赋值，在方法里直接写 `count` 也**拿不到**类变量。
     - `UnboundLocalError` 是 `NameError` 的子类（和 Q3 的继承是同一个道理）。
  3. **没有类似 `static` 的关键字**：Python 只看**前缀**。`count` → 局部变量；`self.count` → 通过对象去找；`Counter.count` → 类本身。`global` / `nonlocal` 分别对应模块级 / 外层函数的变量，**和类变量无关**。以后会学到 `@classmethod` 里的 `cls.count`。
  4. **`self.count += 1` 的遮蔽问题**（我答 `Counter.count` 仍然是 0 ✅）：
     - **读** `self.count`：对象身上没有 → 往类上找 → 找到 0 → 算出 1；
     - **写** `self.count = 1`：赋值永远挂在对象自己身上 → 新建了一个实例变量，把类变量**遮住**了；
     - `Counter.count` 从来没被改过，还是 0。
     ```
     Counter.count ─▶ 0
     a.count       ─▶ 1   （a 自己的实例变量）
     ```
- **结论**：方法里不带前缀的名字 = 局部变量。通过 `self.x` **读**时，找不到会往类上找；但 `self.x = ...` **写**时永远写在对象身上。要修改类变量，必须写 `ClassName.x = ...`。
- **正确写法**：`Counter.count += 1`（⚠️ 这一行我还没自己写出来，下次先自己写）
- **关联**：Q1（`self`）；名字绑定（错题本 #1–#3）；Q3（继承）；→ 错题本 #7、#8

#### Q44 · 什么时候定义函数要写 `self`，什么时候调用时要写 `self.`？（94 中序遍历报 `missing 1 required positional argument`）
- **时间**：2026-11-10 19:45
- **原始问题**：94 二叉树中序遍历，在方法里写了嵌套函数：
  ```python
  def inorderTraversal(self, root):
      def traversal(self, root: Optional(TreeNode)):
          if root is None:
              return []
          traversal(root.left)
          res.append(root.val)
          traversal(root.right)
      res = []
      traversal(root)          # TypeError: ...<locals>.traversal() missing 1 required positional argument: 'root'
      return res
  ```
  「什么时候 function 写 self，什么时候调用函数的时候写 self？」
- **卡点**：把「写在方法里面的嵌套函数」也当成了方法，定义时加了 `self`；调用时只传了一个参数 → `root` 被塞进了 `self`，`root` 就缺了。
- **讲解过程**：
  1. 规则：
     | | 定义时（`def`） | 调用时 |
     |---|---|---|
     | **方法**（直接写在 `class` 里） | 第一个参数写 `self` | `self.方法名(参数)`，括号里不写 self |
     | **普通函数**（包括方法里面的嵌套函数） | 不写 self | `函数名(参数)` |
  2. 为什么调用方法时 self 不进括号：`self.traversal(x)` 会被 Python 变成 `Solution.traversal(self, x)`，**只有 `对象.方法()` 这种写法才会自动传 self**（Q1 的 bound method）。
  3. 报错里的 `<locals>`：`Solution.inorderTraversal.<locals>.traversal` = 「`inorderTraversal` 内部的局部函数」，Python 自己说明它不是方法。
  4. 两种改法：
     ```python
     # 改法一（推荐）：嵌套函数，去掉 self；可以直接用外层的 res
     def inorderTraversal(self, root):
         res = []
         def traversal(root):
             if root is None:
                 return
             traversal(root.left)
             res.append(root.val)
             traversal(root.right)
         traversal(root)
         return res

     # 改法二：写成和 inorderTraversal 平级的方法，用 self. 调用；res 要变成 self.res
     def inorderTraversal(self, root):
         self.res = []
         self.traversal(root)
         return self.res
     def traversal(self, root):
         if root is None:
             return
         self.traversal(root.left)
         self.res.append(root.val)
         self.traversal(root.right)
     ```
     改法二里 `res` 必须变成 `self.res`：`traversal` 是另一个方法，看不到 `inorderTraversal` 的局部变量。
  5. 两个小问题：`Optional(TreeNode)` 要写成 `Optional[TreeNode]`（注解是下标写法，Python 3.13 下圆括号直接 `TypeError: Cannot instantiate typing.Optional`）；`return []` 的返回值没人用，真正收集结果的是 `res.append`，写空 `return` 即可。
- **结论**：`self` 只属于「直接写在 class 里的方法」；嵌套函数是普通函数，不写 self，按名字调用。
- **待办**：检验题：改法一里把 `res.append(root.val)` 换成 `res = res + [root.val]` 还能工作吗？（不能：函数里给 `res` 赋值 → `res` 变成局部变量 → `UnboundLocalError`；`append` 是修改对象，不是重新赋值）
- **关联**：Q1（bound method）、Q6、Q46；→ 错题本 #39、#16（注解圆括号）

#### Q45 · 遍历每个 TreeNode 时想共享一个变量：实例变量、类变量，还是放在「树」上？
- **时间**：2026-11-10 19:52
- **原始问题**：「Tree 里面都是 TreeNode，`__init__` 中有 `self.hi = None`，遍历第一个 Node 时改了 hi，遍历第二个 Node 时访问 hi 是不是还是 None？因为每个 Node 都有一个自己的 hi。如果想维护一个公共变量应该怎么办？应该是 class 变量？怎么写？」
- **卡点**：理解是对的（实例变量每个对象一份），不确定公共变量放在哪、类变量怎么写。
- **讲解过程**：
  1. `self.hi` 是**实例变量**，每个节点一份：`a.hi = 99` 之后 `b.hi` 还是 `None`。
  2. **类变量**：写在 class 里、方法外面，只有一份。
     ```python
     class TreeNode:
         count = 0
         def __init__(self, val):
             self.val = val
             TreeNode.count += 1      # 修改时写类名
     ```
     **坑**：写 `self.count += 1` 等价于 `self.count = self.count + 1` → 右边读到类变量 0，左边赋值却在**实例**上新建了 `count = 1`，把类变量挡住；类上的那份一直是 0。规则：**读可以写 `self.x`，改一定写 `类名.x`**。可变的类变量（列表）用 `self.lst.append()` 会改到公共那份，但容易混淆，不推荐。
  3. **更推荐：放在树上**。这个变量描述的是「整棵树」，就放在 Tree 实例上：
     ```python
     class Tree:
         def __init__(self, root):
             self.root = root
             self.hi = None                # 每棵树一份
         def traverse(self, node):
             if node is None:
                 return
             if self.hi is None or node.val > self.hi:
                 self.hi = node.val
             self.traverse(node.left)
             self.traverse(node.right)
     ```
     类变量是**所有树共用**的，建两棵树会互相干扰。LeetCode 里对应的就是 `self.res`（Solution 上）或「外层局部变量 + 嵌套函数」。
  4. 总结：
     | 放在哪 | 几份 | 适合存 |
     |---|---|---|
     | TreeNode 的 `self.x` | 每个节点一份 | 节点自己的属性（val、left、right） |
     | `TreeNode.x`（类变量） | 所有节点、所有树共用一份 | 真正全局的东西（创建过多少个节点） |
     | Tree / Solution 的 `self.x` | 每棵树（每次求解）一份 | 一次遍历中要共享的状态 ← 最常用 |
  5. 检验题 ✅ 答对：
     ```python
     class A:
         n = 0
         def inc(self):
             self.n += 1
     x, y = A(), A()
     x.inc(); x.inc(); y.inc()
     print(A.n, x.n, y.n)      # 0 2 1
     ```
     查找属性：先找实例，再找类；赋值永远写到实例上 → 类变量 `A.n` 从未被改过。
- **结论**：共享状态先想「它属于谁」：属于整棵树就放在树（或 Solution）的实例上；类变量是所有对象共用，修改时必须写类名。
- **待办**：进阶题未答：接着执行 `A.n = 10; z = A(); print(x.n, y.n, z.n)`（应为 `2 1 10`：x、y 有自己的 n，z 没有，读到类上的 10）
- **关联**：Q6（方法里不带 self 的是局部变量）、Q44、Q46；错题本 #7

#### Q46 · 为什么方法里用类变量也要写 `self.`？类变量和 `__init__` 里的实例变量重名怎么办？（145 后序遍历 `NameError`）
- **时间**：2026-11-10 19:59（追问 20:01）
- **原始问题**：145 后序遍历，把 `res = []` 写成类变量，方法里直接用 `res.append(root.val)` → `NameError: name 'res' is not defined. Did you mean: 'self.res'?`。「为什么 class 变量也要用 self？如果类变量和 instance 变量有重复名称怎么办？可以这么做吗？」追问：「我的意思是如果 `__init__` 中也有变量叫 x，怎么办？」
- **卡点**：以为写在类体里的名字，方法里可以直接用（像外层函数的变量那样）。
- **讲解过程**：
  1. **LEGB 跳过 class**：函数里的裸名字按 Local → Enclosing（外层**函数**）→ Global → Built-in 查找，**类体不在链条里**。所以类变量只能通过 `self.res` 或 `Solution.res` 拿到。对比 Q44：嵌套函数能直接用外层函数的 `res`，因为外层函数属于 E；外层 class 不属于。
  2. **重名**：不报错，**实例变量挡住类变量**：
     ```python
     class A:
         x = "类的"
         def __init__(self):
             self.x = "实例的"      # 每个对象一创建就有了自己的 x
         def show(self):
             print(self.x)          # 实例的
             print(A.x)             # 类的
             print(type(self).x)    # 类的（子类也通用）
     ```
     两份同时存在、互不影响，只是路径不同：`self.x` → 实例的；`A.x` / `type(self).x` → 类的。
     故意这样用的场景：**类变量当默认值**，`__init__` 里只在传了参数时才给对象单独设一份。其他情况尽量**不要重名**。
  3. **把 `res` 写成类变量能跑吗？** 改成 `self.res.append` 能跑通，但有**隐藏 bug**：类变量列表被所有 Solution 实例共用，LeetCode 每个用例都新建 `Solution()`，结果却会累积到同一个列表里（第二棵树的结果里混进第一棵的）。在方法开头写 `self.res = []` 也不行：方法递归调用自己，每进一层都会清空。
  4. 正确写法三选一：
     - A. 嵌套函数 + 外层局部变量 `res`（推荐）
     - B. 入口方法里 `self.res = []`，递归交给另一个方法 `self.traverse`
     - C. 不用共享变量，靠返回值拼接：
       ```python
       def postorderTraversal(self, root):
           if root is None:
               return []
           return (self.postorderTraversal(root.left)
                   + self.postorderTraversal(root.right)
                   + [root.val])
       ```
- **结论**：方法里看不到类体里的名字（LEGB 跳过 class），必须 `self.` / `类名.`；重名时实例变量挡住类变量；可变的类变量会在所有实例间共享，别用来存一次求解的结果。
- **待办**：两道检验题未答：① 写法 B 里把 `self.res = []` 挪到 `traverse` 第一行会怎样？（每进一层递归都清空一次，前面收集的结果被丢掉，只剩最后一小段）② `class B: x = 1; def __init__(self): self.x = self.x + 10` → `print(b.x, B.x)`？（`11 1`：右边读的是类上的 1，左边在实例上新建）
- **关联**：Q6、Q44、Q45；→ 错题本 #40

### Python 语法

#### Q14 · 解包（unpacking）还有哪些用法？
- **时间**：2026-11-03 03:57
- **原始问题**：370 题里讲了 `for start, end, val in operations:` 之后，问「还有类似这样的解包的用法吗，以及常用语法吗？」
- **卡点**：只会用下标 `i[0]`、`i[1]`、`i[2]` 取一行里的元素；不知道 `*` 收集出来的是什么类型。
- **讲解过程**：
  1. **核心规则**：左边几个名字，右边就拆出几个值，按顺序挂上去（名字标签）。个数不对 → `ValueError: too many values to unpack`。
  2. **常用写法**：
     ```python
     a, b, c = [1, 3, 2]              # 基础（列表、元组、字符串都行）
     a, b = b, a                      # 交换：右边先打包成元组 (b, a)，再拆开
     first, *rest = [1, 2, 3, 4]      # rest = [2, 3, 4]
     head, *mid, tail = [1, 2, 3, 4]  # mid = [2, 3]
     start, _, val = [1, 3, 2]        # _ = 这个值我不要
     (a, b), c = [1, 2], 3            # 嵌套
     lo, hi = min_max(nums)           # 函数「返回多个值」其实是返回一个元组
     self.increment(*op)              # 调用时用 * 把列表展开成参数
     print("a", "b", **kwargs)        # ** 把字典展开成关键字参数
     merged = [*a, *b]; d = {**d1, **d2}   # 合并
     ```
  3. **刷题速查**：
     | 场景 | 写法 |
     |---|---|
     | 遍历固定长度的行 | `for a, b, c in rows:` |
     | 下标 + 值 | `for i, x in enumerate(nums):` |
     | 两个列表一起遍历 | `for x, y in zip(xs, ys):` |
     | 字典遍历 | `for k, v in d.items():` |
     | 二维矩阵 | `for i, row in enumerate(mat): for j, x in enumerate(row):` |
  4. **检验题** `a, *b, c = [1, 2]`：答了 `1, 0, 2`，又答 `None`。正确是 `1 [] 2`。→ 错题本 #14
     | 值 | 类型 | 意思 |
     |---|---|---|
     | `0` | `int` | 一个数，值为零 |
     | `None` | `NoneType` | 什么都没有（函数没 `return` 时的返回值） |
     | `[]` | `list` | 一个**存在的**列表，只是没有元素 |
- **结论**：解包 = 按位置把值挂到多个名字上；`*name` **永远得到一个列表**（可能是空列表）。
- **关联**：Q13（370）；错题本 #14

#### Q19 · 字典：一次建多个 key、有没有顺序、为什么不存在的 key 能直接赋值
- **时间**：2026-11-03 10:37（前两问）；2026-11-06 02:53（第三问）
- **原始问题**：①「Python 的字典可以像 list 一样建立多个空的 key value 吗？」②「可以按照顺序来找到相应的 key value 吗？」③（567 题里）「`need[c] = need.get(c, 0) + 1`，原来根本就没有这个 key，为什么能直接赋值 value？」
- **卡点**：把「读字典」和「写字典」当成同一种操作；想用 `d[0]` 按位置取。
- **讲解过程**：
  1. **建多个 key**：
     ```python
     d = {}  /  dict()
     dict.fromkeys(keys, 0)      # {'a': 0, 'b': 0, 'c': 0}；不给值就是 None
     {k: 0 for k in keys}        # 字典推导式
     ```
     ⚠️ `dict.fromkeys(keys, [])` 只造了**一个** `[]`，所有 key 共享（和 `[[0]*3]*3` 同一个坑）→ 用 `{k: [] for k in keys}`。
  2. **key 事先不知道**：`defaultdict(list)` / `defaultdict(int)`，访问不存在的 key 时自动建好 → 不用写 `if key not in d`（中性初始值，见 Q18）。
  3. **顺序**：Python 3.7+ 字典记住**插入顺序**。改值位置不变；删了再插入会移到最后。
     ⚠️ `d[0]` 找的是 key `0`，不是「第一个」→ `KeyError`。按位置取：`list(d)[0]`、`next(iter(d))`（O(n)，经常要按位置取说明该用列表）。按 key 排序遍历：`for k in sorted(d):`。
  4. **读和写规则不同**：
     - **写** `d[k] = v`：key 不存在就**新建**，存在就覆盖。
     - **读** `d[k]`：key 不存在就 **`KeyError`**。
     - `d.get(k, 默认值)`：不存在时返回默认值，**不报错，也不会新建 key**。
  5. `need[c] = need.get(c, 0) + 1`：**先算右边（读，用 get 兜底），再赋值给左边（写，自动新建）**。`t = "aab"` → `{'a': 1}` → `{'a': 2}` → `{'a': 2, 'b': 1}`。
     `need[c] += 1` 不行：等于 `need[c] = need[c] + 1`，右边先读，key 不存在就报错。
  6. **等价写法**：`if c not in need: need[c] = 0`；`defaultdict(int)`；`Counter(t)`。
- **结论**：字典「写」会自动建 key，「读」不会；`get(k, 0)` 用中性初始值让第一次和之后用同一行代码。字典有插入顺序，但不能按位置下标取。
- **待办**：两道检验题还没答：① `d = dict.fromkeys(["a","b"], []); d["a"].append(1); print(d)`（应为 `{'a': [1], 'b': [1]}`）；② `d = {}; x = d.get("k", 0); d["m"] = d.get("m", 10) + 1; print(d, x)`（应为 `{'m': 11} 0`）
- **关联**：错题本 #3（共享引用）；Q18（中性初始值）；Q20、Q21（滑动窗口的计数字典）

#### Q27 · `print()` 在底层是怎么工作的？
- **时间**：2026-11-08 10:20
- **原始问题**：分享了一个 Reddit 帖子（r/learnpython「How does print() work under the hood」），让我总结。帖子本身打不开（reddit.com 被抓取工具和内置浏览器拦截），所以讲的是 CPython 的一般机制，**不是帖子的内容**。
- **讲解过程**：
  1. **变成字符串**：对每个参数调用 `str(x)` → 实际执行 `type(x).__str__(x)`。`print` 自己不知道怎么显示对象，是去问对象本身（Q1 的 bound method）。
  2. **完整签名**：`print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)`（`*objects` 就是解包那一课的「收集参数」）。大致等价于：
     ```python
     file.write(sep.join(str(o) for o in objects) + end)
     if flush: file.flush()
     ```
  3. **`sys.stdout` 只是一个文件对象** → `print("...", file=f)` 可以直接写进文件。
  4. **缓冲**：先写进内存缓冲区；终端通常遇到 `\n` 刷新（行缓冲），文件 / 管道要攒满一块才写 → 有时看不到输出，加 `flush=True`。
  5. **操作系统**：刷新时调用系统调用 `write`，写到文件描述符 1（标准输出），终端再把字节画成字符。
  6. **源码**：`print` 是 C 写的内置函数，在 CPython 的 `Python/bltinmodule.c`（`builtin_print`）；文件写入和缓冲在 `Modules/_io/`。
- **结论**：`print` = `str()` 每个对象 → 用 `sep` 连接、加 `end` → 写进 `file`（默认 `sys.stdout`）→ 缓冲 → 操作系统 → 终端。
- **待办**：① 检验题：`print("a", "b", sep="-", end="!")` 后接 `print("c")`，屏幕显示什么？（应为 `a-b!c`）② 想看帖子原文的话，把正文贴过来再补充。
- **关联**：Q1（`__str__` 走的也是方法查找）、Q14（`*args`）

#### Q28 · `*` 和 `**`：什么时候打包、什么时候解包？`*args` 为什么是元组？
- **时间**：2026-11-08 10:46
- **原始问题**：看到「`print` 的签名 `print(*objects, ...)` 用的就是 `*` 收集参数」，问「这里的 `*` 是代表有 arbitrary 个参数吗？解包是什么？」。之后追问「为什么打印出来是个 tuple？」，总结「所以 `*` 既可以打包又可以解包，具体区分于使用场景」，又说「这个字典的我看不懂」（`**`）。
- **卡点**：把「解包」和「`def` 里的 `*`」当成同一件事；不知道 `*args` 收集出来的是元组；不熟悉关键字参数，所以看不懂 `**`。
- **讲解过程**：
  1. **解包**：一个容器 → 拆成多个名字（`a, b, c = [1, 3, 2]`）。**打包**：多个值 → 装进一个容器。`def f(*args)` 做的是**打包**：任意个位置参数装进一个元组。
     ```python
     def show(*objects): print(type(objects), objects)
     show(1, "hi", 3.5)   # <class 'tuple'> (1, 'hi', 3.5)
     show()               # <class 'tuple'> ()
     ```
  2. **判断规则**：**在「接收」的一边 → 打包；在「给出」的一边 → 解包。**
     | 场景 | 例子 | `*` 的作用 |
     |---|---|---|
     | `def` 的参数（接收） | `def f(*args):` | 打包成**元组** |
     | 赋值左边（接收） | `first, *rest = nums` | 打包成**列表** |
     | 调用函数（给出） | `f(*nums)` | 解包成多个参数 |
     | 字面量（给出） | `[*a, *b]` | 解包成多个元素 |
  3. **检验题** `f(nums)` 和 `f(*nums)`（`f` 里 `print(args)`）：用户先答 `[1,2,3]` + 三行 `1 2 3`，再答 `[1,2,3]` / `1 2 3`。正确是 `([1, 2, 3],)` / `(1, 2, 3)` → 错题本 #29。
     - `f(nums)`：1 个参数（一个列表）→ 元组里只有 1 个元素，`(x,)` 的逗号表示单元素元组，`(5)` 只是数字 5。
     - `f(*nums)`：调用时解包成 `f(1, 2, 3)`，`def` 里再打包成 `(1, 2, 3)`。
     - `1 2 3` 是 `print(*args)` 的输出（再解包一次交给 `print`）。
  4. **为什么是元组**：语言规定。道理：① 参数是调用者传进来的一组固定值，元组不可修改，函数里不会不小心改掉（要改就 `list(args)`）；② 元组更轻、更快，CPython 内部历史上就用元组传位置参数。赋值里的 `*rest` 是列表（PEP 3132），因为拆出来的部分通常还要继续处理。
  5. **关键字参数**：`greet(greeting="Hi", name="Tom")`，按名字对应，顺序随意；`print(..., sep="-", end="!")` 就是。
  6. **`**` = 字典版的 `*`**：
     ```python
     def f(**kwargs): print(kwargs)
     f(sep="-", end="!")          # {'sep': '-', 'end': '!'}   接收 → 打包成字典
     print("a", "b", **options)   # 给出 → 解包成 sep=..., end=...
     {**d1, **d2}                 # 合并，key 重复时后面的覆盖前面的
     ```
     | | 收集什么 | 装进什么 |
     |---|---|---|
     | `*args` | 位置参数 | 元组 |
     | `**kwargs` | 关键字参数 | 字典（key 是参数名的**字符串**） |
  7. **检验题** `h(x=1, y=2)`：答 `{x: 1, y:2}`，正确是 `{'x': 1, 'y': 2}`（key 是字符串；`{x: 1}` 会去找变量 `x`）→ 错题本 #30。
  8. **检验题** `g()`、`g([])`、`g(*[])` 的 `len(args)`：答 `0 1 0` ✅。`g([])` 的空列表本身是 1 个参数。
  9. `**` 刷题时很少用，能看懂即可；重点掌握 `*`。
- **结论**：同一个 `*`，**接收的一边打包、给出的一边解包**；`def` 里的 `*args` 永远是元组，赋值里的 `*rest` 是列表；`**kwargs` 把关键字参数打包成字典，key 是字符串。
- **关联**：Q14（解包）、Q27（`print` 的签名）、Q13（`self.increment(*op)`）；→ 错题本 #29、#30

#### Q31 · Python 的队列能从队尾 pop 吗？`deque`、`list`、`queue.Queue` 的区别
- **时间**：2026-11-08 17:36
- **原始问题**：「Python 中的 queue 可以从队尾 pop 吗？」
- **讲解过程**：
  1. **`collections.deque`（双端队列，刷题首选）**：两头都能放、都能取，全是 O(1)。
     ```python
     q.append(x)      # 右边（队尾）放入
     q.appendleft(x)  # 左边（队头）放入
     q.pop()          # 右边（队尾）取出 ← 默认从右边，和 list.pop() 一样
     q.popleft()      # 左边（队头）取出
     q[0], q[-1]      # 看队头 / 队尾
     ```
  2. **`list`**：`pop()` 从末尾 O(1)；`pop(0)` 从开头 **O(n)**（后面所有元素往前挪）→ 适合当**栈**，不适合当队列。
  3. **`queue.Queue`**：给多线程用（自带锁），只有 `put` / `get`（先进先出），**不能**从队尾取，刷题用不到。
  4. 结论：**栈用 `list`，队列用 `deque`**。
- **待办**：检验题：`q = deque(); q.append(1); q.append(2); q.appendleft(3); print(q.pop(), q.popleft(), list(q))`（应为 `2 3 [1]`）
- **关联**：Q15（删除开头元素要挪位置）、Q17（栈）、Q32（单调队列）

#### Q33 · 为什么遍历哈希表时不能依赖 key 的顺序？
- **时间**：2026-11-08 17:36
- **原始问题**：贴了一段 Java 伪代码（遍历底层 `table` 数组、收集非空格子的 key）和一段讲解文字，问「这段代码在干什么？这在讲解什么？」
  ```java
  for (int i = 0; i < table.length; i++) {
      KVNode node = table[i];
      if (node != null) keys.add(node.key);
  }
  ```
- **讲解过程**：
  1. **哈希表底层就是一个数组**：`put(key, value)` → `hash(key) % table.length` 算出下标 → 存到 `table[下标]`。大部分格子是空的。
  2. **遍历 = 从头到尾扫 `table`，收集非空格子的 key** → 遍历顺序 = key 在数组里的**下标顺序**，和插入顺序无关。（简化版：真实实现一个格子可能挂多个冲突节点。）
  3. **顺序不可靠的两个原因**：① hash 函数把 key 打散，下标看起来随机；② 扩容时 `table.length` 变了，`hash(key) % 新长度` 变了 → 所有元素重新搬家 → 增删几个元素后顺序可能完全不同。
  4. **Python 的特例**：`dict`（3.7+）保持插入顺序——CPython 把 `(key, value)` 按插入顺序存在一个紧凑数组里，哈希部分只存下标，遍历扫的是那个有序数组。`set` 没有这个保证。Java 的 `HashMap` 就是文中说的无序。
- **结论**：遍历顺序 = 底层存储的顺序。知道底层怎么存，就能推出顺序可不可靠，不用背。
- **待办**：检验题：从底层解释为什么不能用 `d[0]` 取字典的「第一个」，而列表可以 `a[0]`。
- **关联**：Q19（字典的插入顺序）、Q34

#### Q34 · 128 最长连续序列：代码里没用 map，为什么说用了哈希？`set` / `dict` 的查找都是 O(1) 吗？
- **时间**：2026-11-08 17:36
- **原始问题**：看 LeetCode 128 官方题解，「明明代码中没有使用 map，为什么还说使用哈希？难道 set 内部也有哈希？」之后：「所以 set 和 dict 的查找都是 O(1)？」
- **讲解过程**：
  1. **`set` 内部就是哈希表**，只存 key、不存 value（「只要 key 的 dict」）。`dict` → 「key 对应的值是多少」；`set` → 「这个东西在不在」。Java 里对应 `HashMap` / `HashSet`。
  2. **128 为什么必须用哈希**：核心操作是反复问「某个数在不在」。
     ```python
     num_set = set(nums)
     for num in num_set:
         if num - 1 not in num_set:       # 只从连续段的起点开始数
             cur = num
             while cur + 1 in num_set:
                 cur += 1
     ```
     `list` 的 `in` 是 O(n)（逐个比较）→ 整体 O(n²)；`set` 的 `in` 是算 `hash(x)` 直接跳到格子 → 平均 O(1) → 整体 O(n)。
  3. **可哈希才能放进 set / 当 dict 的 key**：数字、字符串、元组可以；`list`、`dict` 不行（`TypeError: unhashable type`），因为可变，改了以后哈希值就对不上。
  4. **O(1) 的两个限定**：
     - **平均** O(1)：哈希冲突多时（很多 key 挤在同一格）最坏 O(n)；实际刷题当 O(1) 用，写「平均 O(1)」。
     - **按 key 查**才是 O(1)：`2 in d.values()` 是 O(n)。
  5. **速查**：
     | 操作 | `list` | `set` / `dict` |
     |---|---|---|
     | `x in`（按 key） | O(n) | 平均 O(1) |
     | 添加 | `append` O(1) | 平均 O(1) |
     | 删除 | `remove(x)` O(n) | 平均 O(1) |
     | 按位置 `[i]` | O(1) | ❌ |
     | 顺序 | 有 | dict 有（插入顺序），set 没有 |
  6. **套路**：需要反复问「在不在」→ 先把列表转成 `set`，用 O(n) 空间换 O(1) 查找。
- **结论**：「用哈希」不一定是 map；`set` 和 `dict` 底层都是哈希表，按 key 查找平均 O(1)。
- **待办**：检验题：删掉 `if num - 1 not in num_set`，结果还对吗？`[1, 2, 3, 4]` 里 `while` 共执行几次？复杂度变成多少？（结果仍对，但会退化成 O(n²)）
- **关联**：Q19、Q33；Q8（均摊分析：每个数只被 `while` 走过一次）

#### Q35 · 我对 `dict` / `set` 底层的总结对吗？
- **时间**：2026-11-08 17:55
- **原始问题**：用户贴出自己的总结：「dict、set 底层都使用了 hash，dict 通过 hash 计算出来了 key，然后在对应的数组位置存储了 (key:value)；set 通过 hash 计算出来了 key，只在对应的位置存储了 key。所以二者在平均情况下搜索查找都是 O(1) 的时间消耗。」
- **卡点**：「hash 算出 key」的说法颠倒了因果。
- **讲解过程**：
  1. hash 函数**不是算出 key**，而是**用 key 算出数组下标**。key 是本来就有的。
  2. 修正版：`dict` 和 `set` 底层都是哈希表，用 hash 函数**根据 key 算出数组下标**；`dict` 在这个位置存 `(key, value)`，`set` 只存 `key`。按 key 查找时直接算出下标去看，平均 O(1)（冲突多时最坏 O(n)）。
     ```
     key ──hash()──▶ 一个大整数 ──% table 长度──▶ 下标 ──▶ table[下标]
     "apple"         8342917…                     731       (apple, 1)  ← dict
                                                            apple       ← set
     ```
  3. 两个补充：
     - **「按 key」很重要**：`2 in d.values()` 是 O(n)，value 没参与 hash，没有下标可算。
     - CPython 的 `dict` 多了一层：`(key, value)` 按插入顺序存在紧凑数组里，哈希表只存「在紧凑数组里的第几个」→ `dict` 有插入顺序，`set` 没有。
- **结论**：hash 是「key → 下标」的映射；`dict` 存键值对、`set` 只存键，按 key 查找平均 O(1)。
- **待办**：检验题未答：为什么 `list` 不能当 `dict` 的 key / 放进 `set`？（用「key → hash → 下标」解释：放进去以后改了列表，hash 变了，去新下标找不到原来存的位置）
- **关联**：Q33、Q34

#### Q36 · `head: Optional[ListNode]` 是什么类型？`Optional` 是什么？难道不是 list？
- **时间**：2026-11-08 19:33
- **原始问题**：看 142 环形链表 II 的函数签名：「`head: Optional[ListNode]` 这个我怎么没看懂是什么类型呢？Optional 是什么鬼，难道不是 list？」
- **卡点**：把 `ListNode` 当成了 Python 的 `list`；不认识 `Optional`。
- **讲解过程**：
  1. **`ListNode` 是自定义的类**（代码顶部注释掉的就是它的定义，LeetCode 后台已定义好）：每个对象存一个 `val`，用 `next` 指向下一个节点。参数 `head` 只是**第一个节点**，不是整条链表；后面的节点只能沿着 `next` 一步步走（`head.next.next.val`）。
     | | `list` | 链表（`ListNode`） |
     |---|---|---|
     | 传进来的是 | 整个容器 | 只有第一个节点 |
     | 取第 i 个 | `a[i]`，O(1) | 从 head 走 i 步，O(n) |
     | 下标 `[ ]` | 有 | 没有 |
     题目里的 `head = [3,2,0,-4]` 只是给人看的输入格式，LeetCode 会先转成一串节点。
  2. **`Optional[X]` = 「X 或者 None」**，等价于 `Union[X, None]`、`X | None`（3.10+）。链表里 None 无处不在：空链表 `head = None`、返回「没有就 null」、最后一个节点的 `next = None`。
  3. **类型注解只给人看**，运行时不检查。真正要做的是访问 `.next` / `.val` 之前确认不是 None：`while fast and fast.next:`（`and` 短路）。
- **结论**：`ListNode` 是节点类，`head` 是第一个节点；`Optional[ListNode]` 读作「一个节点，或者 None」。
- **待办**：检验题未答：`a.next = b` 之后 `print(a.next.next)` → `None`；`print(a.next.next.val)` → `AttributeError: 'NoneType' object has no attribute 'val'`
- **关联**：Q1（`a.next = b` 也是名字标签）、Q37、Q40；错题本 #16（注解写法）

#### Q40 · `not head` 和 `head is not None` 不是一回事吗？
- **时间**：2026-11-09 14:30
- **原始问题**：修 23 题 `[[]]` 的 bug 时，我问「这一行前面应该加什么判断」，用户反问：「`not head` 和 `head is not None` 不是一回事吗？」
- **卡点**：把两个**意思相反**的表达式当成了同一个。
- **讲解过程**：
  1. 代入两种情况：
     | `head` | `not head` | `head is not None` |
     |---|---|---|
     | `None` | `True` | `False` |
     | 一个节点 | `False` | `True` |
  2. 真正等价的两组：「是空的」→ `not head` ⇔ `head is None`；「不是空的」→ `head`（直接写）⇔ `head is not None`。
  3. 23 题两种写法都行：
     ```python
     for i, head in enumerate(lists):
         if head is not None:              # 或 if head:
             heapq.heappush(pq, (head.val, i, head))
     # 或者
     for i, head in enumerate(lists):
         if not head:                      # 或 if head is None:
             continue
         heapq.heappush(pq, (head.val, i, head))
     ```
  4. **`if x:` 和 `if x is not None:` 什么时候不一样**：`if x` 看真值，`0`、`""`、`[]` 都是假的；`is not None` 只排除 None。节点对象真值永远 True，所以链表里两者等价；但「返回下标，没找到返回 None」的函数，下标 0 用 `if r:` 会被当成「没找到」。
- **结论**：`not head` ⇔ `head is None`，和 `head is not None` 正好相反；只想排除 None 时用 `is None` / `is not None` 最准确。
- **待办**：检验题未答：`r = find([5, 6, 7], 5)`（返回 0）→ `if r:` 打印什么？（打印「没找到」，错；应改成 `if r is not None:`）
- **关联**：Q16（判断列表是否为空）、Q36、Q39；→ 错题本 #36

#### Q64 · 797 所有路径里 `self.path.copy()` 不应该用深拷贝吗？浅拷贝存的不还是引用？赋值到底改的是什么？
- **时间**：2026-11-13 17:50（追问 17:53、17:54、17:55、17:57、18:02、18:04）
- **原始问题**：797 回溯代码里 `self.res.append(self.path.copy())`：「这难道不应该使用深拷贝嘛？path 后面还会改变，如果是 shallow copy 的话，前面存储的就会被改变吧。」追问：「浅拷贝不是还是存入引用吗？」「我觉得 `self.path.copy()` 就是创建一个新的对象，这个对象存储 path 的引用地址。」「那深拷贝呢？」「所以嵌套列表时深浅就有区别了，浅拷贝出来的对象里存储的共享变量可以改变。」用户总结后问：「为什么 `b[1] = [100]` 不能进行共同的改变？根本原因是什么？」「所以说 assignment 是改变地址？」
- **卡点**：以为浅拷贝的新列表里存的是 **path 本身的地址**（那就和不拷贝一样了）；分不清「改格子」和「改对象」。
- **讲解过程**：
  1. 三种写法：
     - `res.append(path)`：不拷贝，res 里全是同一个 path 对象，回溯结束 path 被 pop 空 → `[[], [], ...]` ❌
     - `res.append(path.copy())`：新建列表，后面 `path.append/pop` 改的是旧列表 ✅
     - `deepcopy(path)`：也对，但 path 里是整数，多余且慢
  2. **浅拷贝存的是元素的地址，不是 path 的地址**：
     ```
     path   ──▶ [ •, •, • ]      列表 A
                  │  │  │
                  0  1  3        ← 元素共享
                  │  │  │
     res[0] ──▶ [ •, •, • ]      列表 B（新的，有自己的格子）
     ```
     相当于 `new = []; for x in path: new.append(x)`，拷完和 path 再无连接。验证：`b is path` → False；`b[0] is path[0]` → True；`path.pop()` 后 b 不变。
  3. **深拷贝**：元素是容器时递归往里复制：
     ```python
     a = [[1, 2], [3]]
     b = a.copy(); c = copy.deepcopy(a)
     b[0] is a[0]   # True
     c[0] is a[0]   # False
     a[0].append(99)
     # b → [[1, 2, 99], [3]]，c → [[1, 2], [3]]
     ```
     | | 外层 | 内层元素 | 用在 |
     |---|---|---|---|
     | `x = a` | 同一个 | 同一个 | 只想多个名字 |
     | `a.copy()` | 新 | 共享 | 元素不可变，或只增删外层 |
     | `deepcopy(a)` | 新 | 新（递归） | 元素可变且之后会被修改 |
     `deepcopy` 遇到不可变对象直接复用。
  4. **根本原因：赋值改格子，方法改对象**：
     - `b[0].append(99)`：顺着 B 的格子 0 找到共享对象 `[1, 2]`，**修改对象本身** → A 也看得到。
     - `b[1] = [100]`：新建 `[100]`，把 **B 的格子 1** 里的地址换掉；`[3]` 和 A 都没被碰 → A 不变。
     共享的是内层对象，**格子不共享**。
  5. **赋值 = 改「某个名字 / 格子 / 属性」里存的地址，从不修改原来指向的对象**：`x = ...`、`b[1] = ...`、`node.next = ...`。
  6. **例外 `+=`**：对列表，`b += [3]` 等价于 `b.extend([3])`，先原地修改再赋回同一地址 → 共享这个列表的 a 也变；`b = b + [4]` 是新建列表。对 int / str / tuple，`+=` 只能新建对象再换地址（所以 `self.count += 1` 会在实例上新建变量，见 Q45）。
- **结论**：浅拷贝 = 新容器 + 共享元素；只增删外层或元素不可变时浅拷贝就够。`=` 换地址，方法调用（`append` / `pop` / `extend`）和对列表的 `+=` 改对象。
- **待办**：
  - 检验题未答：`path = [0, 1]; res.append(path); res.append(path.copy()); path.append(3); print(res)`（`[[0, 1, 3], [0, 1]]`）
  - 检验题未答：`grid = [[0] * 3] * 2; grid[0][0] = 1` 输出？（`[[1, 0, 0], [1, 0, 0]]`：外层两个格子指向同一个内层列表，原地修改；正确写法 `[[0] * 3 for _ in range(2)]`，同错题本 #3）
- **关联**：Q1（赋值 = 移动名字标签）、Q45、Q47（`cur = dq[0]`）；错题本 #1、#2、#3、#41；→ 错题本 #51

#### Q66 · `d = [[0, -1], [0, 1], [-1, 0], [1, 0]]; for dx, dy in d:` 合法吗？
- **时间**：2026-11-18 16:08
- **原始问题**：「`d = [[0, -1], [0, 1], [-1, 0], [1, 0]]` / `for dx, dy in d:` 这样合法吗？」
- **卡点**：不确定 for 里能不能直接把内层列表拆开。
- **讲解过程**：
  1. 合法，就是**解包**（和 `for i, x in enumerate(...)` 同一个机制）：每轮取出一个元素 `[0, -1]`，相当于 `dx, dy = [0, -1]`。
  2. 典型用法：网格 DFS / BFS 走上下左右：
     ```python
     for dx, dy in d:
         nx, ny = x + dx, y + dy
         if 0 <= nx < m and 0 <= ny < n:   # 先检查越界
             ...
     ```
  3. 注意：内层元素个数必须正好是 2，否则 `ValueError: too many values to unpack`；更常见写成元组 `[(0, -1), ...]`，表示固定不变的一对值；注意 x 是行还是列（错题本 #10）。
- **结论**：for 循环里可以按位置解包，内层元素个数要和变量个数一致。
- **待办**：检验题未答：`for i, (dx, dy) in enumerate(d):` 合法吗？第一轮 i、dx、dy 是多少？（合法，嵌套解包；`0, 0, -1`）
- **关联**：Q14 / Q19（解包）、Q67（130 里用到）

#### Q69 · `sort` 的 `key` 参数是什么类型？`lambda` 为什么用在这里？`key=len` 又是什么？为什么 key 必须是函数？
- **时间**：2026-11-18 16:57（追问 16:58；11-23 15:41 再问「为什么必须是函数」）
- **原始问题**：1135 最低成本连通所有城市的 Kruskal 代码里 `connections.sort(key=lambda x: x[2])`：「这个 lambda 为什么在这里用？sort 的参数 key 的类型是什么？」追问：「`words.sort(key=len)` 这是啥？」后来又问：「key 是个函数？？为什么 sort 的这个参数必须要用一个函数？」
- **卡点**：不知道函数可以当参数传；不理解 sort 为什么要的是函数而不是一个值。
- **讲解过程**：
  1. **`key` 是一个函数**（可调用对象，`Callable[[元素], 可比较的值]`，默认 None）。sort 对每个元素调用一次它，**按返回值排序**，不是按元素本身。
     ```python
     connections = [[1, 2, 5], [1, 3, 1], [2, 3, 3]]
     connections.sort(key=lambda x: x[2])   # key: 5, 1, 3 → [[1,3,1], [2,3,3], [1,2,5]]
     ```
  2. **`lambda` = 没有名字的小函数**，只能写一个表达式，值就是返回值：`lambda x: x[2]` ⇔ `def get_weight(x): return x[2]`。一次性的小函数不值得起名。
  3. **为什么这里要 key**：不传 key 时列表按字典序比较（先比 u），Kruskal 要按权重从小到大挑边。
  4. **`key=len`**：把内置函数 `len` **本身**交出去，sort 对每个元素调用 `len(w)`，等价于 `key=lambda w: len(w)`。注意是 `key=len` 不是 `key=len()`：后者当场调用、没给参数 → `TypeError`。我们要「把函数交出去让别人调用」，所以不加括号。`key=abs`、`key=str.lower` 同理。
  5. **为什么必须是函数**：sort 要的是一条**规则**，不是一个值。元素很多、每个的排序依据不同，写代码时还不知道有哪些元素 → 只能给一个「拿到任意元素就能算出依据」的方法，也就是函数。sort 内部大致是 `keys = [f(x) for x in lst]` 再按 keys 排。类比：让图书管理员「按页数排」是一个对每本书都适用的方法，「按 5 排」听不懂。
  6. 函数也是对象，可以赋值、传参（Q1 的 bound method 同理）。同样的模式：`max(words, key=len)`、`min(..., key=...)`、`heapq.nsmallest(k, items, key=...)`。
- **结论**：`key` 接收一个「元素 → 排序依据」的函数；lambda 是写这种一次性小函数的简写；传函数时不加括号。
- **待办**：检验题未答：`words = ["banana", "kiwi", "apple"]; words.sort(key=len)` → ？（`["kiwi", "apple", "banana"]`，按长度 4、5、6）
- **关联**：Q1（函数是对象）、Q70、Q78；错题本 #16（漏 `()` 的反面）

#### Q70 · `sort` 默认是从小到大吗？怎么反过来？
- **时间**：2026-11-18 16:59
- **原始问题**：「sort 默认是小到大？怎么反转？」
- **卡点**：无，新知识点；顺带发现 210 代码里的 `reverse()` 用法错误。
- **讲解过程**：
  1. 默认升序；降序加 `reverse=True`：`nums.sort(reverse=True)`、`words.sort(key=len, reverse=True)`、`sorted(nums, reverse=True)`。
  2. 数字也可以把 key 取负：`key=lambda x: -x`。真正有用的是**多条件、方向不同**时：`key=lambda p: (p[1], -p[0])`（`reverse=True` 会把所有条件一起反过来）。
  3. 别和 `list.reverse()` 混：
     | 写法 | 做什么 | 返回值 |
     |---|---|---|
     | `a.sort(reverse=True)` | 排序，降序 | `None`（原地） |
     | `a.reverse()` | 不排序，只把现有顺序倒过来 | `None`（原地） |
     | `sorted(a, reverse=True)` | 排序 | 新列表 |
     | `a[::-1]` | 倒序 | 新列表 |
  4. 210 课程表代码里 `reverted_res = self.res.reverse()` 拿到的是 `None` → 应先 `self.res.reverse()` 再 `return self.res`，或 `return self.res[::-1]`。
- **结论**：`reverse=True` 降序；原地修改的方法（`sort`、`reverse`、`append`）都返回 None，不要用它们的返回值。
- **待办**：检验题未答：`a = [3, 1, 2]; b = a.sort(); print(a, b)` →？（`[1, 2, 3] None`）
- **关联**：Q69、Q78；→ 错题本 #53

#### Q73 · hash set 和 hash map 的区别：set 也会做 hash 映射吗？存什么？会处理冲突吗？
- **时间**：2026-11-20 10:48（追问 10:49）
- **原始问题**：「hash set 和 hash map 的区别，hashmap 会根据 key 进行 hash 映射，在对应的地方存储相应的 value，那 hash set 呢？会进行映射吗？存储什么？」追问：「所以它不会解决 hash 冲突？」
- **卡点**：以为 set 不存 value，就连冲突处理也省了。
- **讲解过程**：
  1. 同一套机制，只差存什么：
     | | 拿什么算 hash | 在那个位置存 |
     |---|---|---|
     | `dict` | key | `(key, value)` |
     | `set` | 元素本身（元素就是 key） | 只存 key |
     set ≈ 只有 key 的 dict，只回答「在不在」；`add` 已存在就什么都不做 → 自动去重。Java 的 `HashSet` 内部就是一个 `HashMap`，value 放占位对象。
  2. **冲突发生在「算下标」这一步**，和存不存 value 无关，所以 set 一样要处理。例子：CPython 里 `hash(-1) == hash(-2)`（都是 -2），但 `{-1, -2}` 两个都在。
  3. 两种解决方法：
     | 方法 | 做法 | 谁在用 |
     |---|---|---|
     | 开放寻址 | 位置被占就按规则探测下一个位置 | CPython `dict` / `set` |
     | 拉链法 | 每个位置挂一条链表 | Java `HashMap` / `HashSet` |
     查找：算下标 → 那里的元素 `== x` 吗 → 不是就继续探测 / 沿链表走，碰到空位才说明不在。所以元素需要 `__hash__`（算下标）和 `__eq__`（确认是不是它）。冲突多时退化成逐个比较 → 最坏 O(n)。
- **结论**：set 和 dict 都是「key → hash → 下标」，set 只省掉了 value，不省冲突处理。
- **待办**：Q35 那道检验题仍未答：为什么 `list` 不能放进 set？（放进去之后再 `append`，hash 变了，去新下标找不到原来存的位置）
- **关联**：Q35、Q33、Q34；→ 错题本 #57

#### Q78 · `envelopes.sort(key=lambda x: (x[0], -x[1]))`：lambda 为什么返回元组？是 sort 特有的吗？
- **时间**：2026-11-23 15:39
- **原始问题**：354 俄罗斯套娃信封：「这是什么意思？lambda 这个 expression 为什么是一个 tuple？这有啥用吗？还是说这是 sort 函数特有的 key？」
- **卡点**：不知道 key 可以返回元组，以为是 sort 的特殊语法。
- **讲解过程**：
  1. 不是 sort 特有，用到两条通用规则：key 可以返回**任何能比较大小的值**；**元组逐位比较**（先比第 0 位，相等才比第 1 位）。`(2, 5) < (3, 1)` True，`(2, 5) < (2, 7)` True。23 题堆里的 `(val, i, node)` 同理。
  2. 这一行的意思：**先按宽升序，宽相同时按 `-高` 升序 = 高降序**。
     ```
     [[5,4], [6,4], [6,7], [2,3]] → key (5,-4) (6,-4) (6,-7) (2,-3)
     排序后 [2,3], [5,4], [6,7], [6,4]
     ```
     取负是为了让第二个条件反方向（`reverse=True` 做不到一升一降）。
  3. **354 为什么这样排**：宽已递增 → 问题变成高度序列的最长严格递增子序列（LIS）。同宽不能套，如果同宽时高度升序（`[6,4], [6,7]`），LIS 会误选 4 → 7；同宽时高度降序（7 → 4），LIS 不可能同时选中两个同宽信封。
- **结论**：key 返回元组 = 多级排序；负号让某一级反方向排。
- **待办**：检验题未答：`[[1,2], [1,5], [0,9]]` 按 `(p[0], -p[1])` 排序后？（`[[0,9], [1,5], [1,2]]`）
- **关联**：Q69、Q70；Q39（23 题元组比较）

### 刷题 / LeetCode

#### Q2 · LeetCode 1314 矩阵区域和：检查我的思路
- **时间**：2026-11-02 10:02
- **原始问题**：给定 `m x n` 矩阵 `mat` 和整数 `k`，返回 `answer`，其中 `answer[i][j]` 等于所有满足 `i-k ≤ r ≤ i+k`、`j-k ≤ c ≤ j+k`、且 `(r, c)` 在矩阵内的 `mat[r][c]` 之和。我的思路：先拿到 `mat` 的行数和列数 → 建一个同形状的空 `answer` → 二重循环遍历每个格子，每个格子调用一个 `Sum` 函数（传入 `mat` 和 `k`，内部用二重循环求和）。问题：行数和列数怎么拿？
- **卡点**：
  1. 不知道怎么拿行数和列数。
  2. `Sum` 只传了 `mat` 和 `k`，不知道当前算的是哪个格子。
  3. 边界：上界写成了 `min(m, i + k)`（off-by-one，见错题本 #4）。
  4. 空矩阵用 `[[0]*3]*3` 建（三行共享同一个列表，见错题本 #3）。
- **讲解过程**：
  1. `m = len(mat)`（行数 = 内层列表的个数），`n = len(mat[0])`（列数 = 第一行的长度）。
  2. `Sum` 还要接收 `i, j`，才知道是哪个格子的窗口。
  3. 边界要夹住：`mat[-1]` 不会报错，会悄悄读到**最后一行**，所以结果错了也没有报错提示。
     ```python
     r_start = max(0, i - k);  r_end = min(m - 1, i + k)   # 闭区间，包含 r_end
     c_start = max(0, j - k);  c_end = min(n - 1, j + k)
     for r in range(r_start, r_end + 1):
         for c in range(c_start, c_end + 1):
             ...
     ```
     等价写法（开区间）：`range(max(0, i-k), min(m, i+k+1))`。两种选一种，**不要混用**。
  4. 建空矩阵：`answer = [[0] * n for _ in range(m)]`（每一行都是新列表）。
  5. 复杂度：每个格子要加 `(2k+1)²` 个数，最坏约 100⁴ = 10⁸ 次运算，Python 可能会超时。→ 下一步：**二维前缀和**。
- **结论**：思路结构没问题（遍历每个格子 + 求一个格子的和的辅助函数），关键在于：用 `len` 拿形状、给辅助函数传 `(i, j)`、用 max/min 夹边界且全程只用一种区间写法、每行单独建一个新列表。
- **关联**：二维列表、`range` 的边界、名字绑定（错题本 #3）；下一步：前缀和
- **状态**：暴力解法已写（见 Q4），还有 3 个 bug 待修

#### Q4 · 1314 暴力解法的代码审查：`NameError` 和命名规范
- **时间**：2026-11-02 10:36
- **原始问题**：第一版代码（节选）运行时报 `NameError: name '__Sum__' is not defined. Did you mean: 'self.__Sum__'?`；追问：`__Sum__` 这样命名对吗？
  ```python
  answer = [[0]*m]*n                         # 第 13 行
  ...
  answer[i][j] = __Sum__(mat, k, i, j)       # 第 16 行
  def __Sum__(mat, k, r, c):                 # 第 19 行（类里的方法）
      r_start = max(0, r-k); r_end = min(len(mat)-1, r+k)   # 边界正确 ✅
      ...
  ```
- **找到的 bug**：
  1. **`NameError`**：方法挂在类上，不是一个独立的名字 → 要写成 `self._block_sum(...)`。
  2. **定义里漏了 `self`**：`self.x(mat, k, i, j)` 会变成 `Solution.x(self, mat, k, i, j)`，一共 5 个参数，而定义只有 4 个 → `TypeError`。这正是 Q1 里那道「忘写 `self` 会怎样」的题。
  3. **第 13 行**：`[[0]*m]*n` → 犯了错题本 #3 的坑，而且 `m`、`n` 写反了（3×3 的例子看不出来，2×3 就会出错）。应写成 `[[0] * n for _ in range(m)]`。
- **命名规范**：
  | 写法 | 例子 | 含义 |
  |---|---|---|
  | `_name` | `_block_sum` | 内部辅助方法，只是约定 ← **辅助方法用这个** |
  | `__name` | `__block_sum` | 名字改写（变成 `_Solution__block_sum`），很少需要 |
  | `__name__` | `__init__`、`__len__` | **留给 Python 自己的特殊方法**，不要自己发明 |
  - PEP 8：函数 / 方法名用 `lowercase_with_underscores`；首字母大写留给类名；不要用 `sum` / `_sum`，会和内置函数 `sum` 混淆。
  ```python
  def _block_sum(self, mat, k, r, c): ...
  answer[i][j] = self._block_sum(mat, k, i, j)
  ```
- **结论**：类里的辅助方法要用 `self.` 调用，定义时第一个参数也要写 `self`；名字用 `_lower_snake`，不要用 `__dunder__`。
- **关联**：Q1（`self`、bound method）；错题本 #3、#6
- **第二版（10:52）**：调用时加了 `self.`，定义里补上了 `self`，`n`、`m` 顺序也对了 ✅。但还是写成 `answer = [[0]*n]*m` → 示例 1 返回 `[[24,39,28]] * 3`（见错题本 #3 的更新）。辅助方法名还是 `__sum__`（还是 dunder 形式）→ 应改成 `_block_sum`。
- **状态**：最后一个修改（改用列表推导式）在本地验证过，示例 1 的结果正确；还没在 LeetCode 上提交
- **复杂度分析**（2026-11-02 13:37）：
  - 我先答「时间 O(n²)」→ 提示：有四层嵌套循环 → 改答「O(n⁴)」✅（最坏情况）
  - 精确写法：O(m · n · min(m, 2k+1) · min(n, 2k+1))；`k` 小时约 O(mn·k²)；`k` 大时（窗口盖住整个矩阵）是 O(m²n²)，`m = n` 时就是 n⁴；`m = n = 100` 约 10⁸ 次加法 → Python 可能超时。
  - 空间：算上 `answer` 是 O(mn) ✅；**不算输出的额外空间**这个问题还没回答（答案提示：`_block_sum` 里只有几个整数变量）。
  - 慢的根源：相邻格子的窗口几乎完全重叠，却每次都从头加起 → **二维前缀和**能把时间降到 O(mn)（下一步要学）。

#### Q7 · 1314 二维前缀和版本：`NameError`、坐标约定、读懂题解
- **时间**：2026-11-02 14:24
- **原始问题**：自己写了前缀和版本（`Solution.matrixBlockSum` 里调用一个单独的类 `NumMatrix`，对应 LeetCode 304）。先问「什么情况」（`NameError`），再问「哪里有错误」，然后追问：「x 难道不是用来表示横坐标（列）吗？」「我两边都想让 x 表示横坐标」「为什么构造 `preSum` 的那个循环不受影响？」最后贴了一份题解问「他这是怎么想的」。
- **卡点**：
  1. `NameError: name 'mat' is not defined`，出现在 `NumMatrix.__init__` 的第 29 行。
  2. 修好之后：示例 1 返回 `None`。
  3. 补上 `return` 后，结果是期望答案的**转置**；用 2×3 矩阵会报 `IndexError`。
  4. 理解不了「x 明明是横坐标，为什么放进 `preSum[x][y]` 就错了」。
- **讲解过程**：
  1. **读 traceback**：从下往上读 → `NumMatrix(mat)` → 进入 `__init__` → 第 29 行报错。`mat` 是 `matrixBlockSum` 的**局部变量**（参数），在 `NumMatrix.__init__` 里看不到。传过去的列表对象在那边叫参数名 `matrix`（Q6 的局部变量规则）。
  2. **函数忘了 `return`** → 默认返回 `None`（错题本 #9）。
  3. **二维列表的下标顺序**：`mat[a][b]` 是先 `mat[a]` 选**第 a 行**（纵向），再 `[b]` 在这一行里选**第 b 个**（横向）。所以**第一个下标 = 纵坐标（行），第二个下标 = 横坐标（列）**，和数学里写 `(x, y)` 的顺序正好相反。
  4. **我的 bug**：`matrixBlockSum` 里让 `x ← j`（x = 列），但 `sumRegion` 里写的是 `preSum[x][y]`（x 放在了行的位置）→ 两套约定 → 结果被转置。正方形矩阵不会越界，结果只是悄悄错了；非正方形矩阵会直接越界。
  5. **两种一致的改法**：
     - 「x = 横坐标（列）」：在 `sum_region` 里写 `p[y][x]`：`p[y2+1][x2+1] - p[y1][x2+1] - p[y2+1][x1] + p[y1][x1]`。规则：**x、y 是给人看的坐标，二维列表的下标永远是 `[y][x]`（先纵后横）**。
     - 「x = 行（矩阵下标的习惯）」：`x ← i`、`y ← j`，直接写 `preSum[x][y]`（题解就是这样做的）。
     - 或者干脆用 `row1, col1, row2, col2`，没有歧义。
     - 名字只是标签，Python 不知道 x 该表示什么。一个名字如果让人每次都要停下来想「这里 x 到底是行还是列？」，它就是坏名字。
  6. **为什么构造 `preSum` 的循环不受影响**：`i` 永远在第一个位置、上限是 `m`；`j` 永远在第二个位置、上限是 `n` → 只有一套约定。之前的 bug 出在**两套约定交接的地方**（函数之间传参数时，x 的含义悄悄变了）。
     > 规律：bug 往往出现在**两套约定交接的地方**：函数参数、换名字、换坐标系。
  7. **读懂题解**（x = 行，y = 列，从头到尾只有一套约定）：
     - `preSum[i][j]` = 原矩阵中 `[0..i-1] × [0..j-1]` 这个矩形的和。多出的一行一列全是 0（代表空矩形），所以不需要判断边界。
     - **构造**：`preSum[i][j] = 上 + 左 + 当前格 − 左上`（左上那块被加了两次）
       ```
       ┌───────┬───┐   上   = A + B
       │   A   │ B │   左   = A + C
       ├───────┼───┤   左上 = A
       │   C   │ ● │   ● = matrix[i-1][j-1]
       └───────┴───┘
       ```
     - **查询**：`D = 大 − 上 − 左 + 左上`
       ```
       preSum[x2+1][y2+1] = A+B+C+D    preSum[x1][y2+1] = A+B
       preSum[x2+1][y1]   = A+C        preSum[x1][y1]   = A
       ```
       要**包含**第 x2 行 → 用 `x2+1`；要**不含**第 x1 行 → 用 `x1`（因为 `preSum` 的下标表示「到前一行为止」）。
  8. 复杂度：构造 O(mn) + 每次查询 O(1) × mn 个格子 = **O(mn)** 时间；`preSum` 占 O(mn) 额外空间。
- **结论**：前缀和 = 先花 O(mn) 预处理，之后每个区域的和都能 O(1) 查出来。坐标约定可以任选，但**全程只能有一套**。二维列表永远是 `[行][列]`。
- **待办**：① 用示例 1 的中心格 `(1, 1)` 手算一遍 `sumRegion` 的四项，看结果是不是 45；② 检验题：把构造循环改成 `range(1, n+1)` / `range(1, m+1)`，3×3 和 2×3 分别会怎样？③ 提交到 LeetCode。
- **关联**：Q4、Q6（局部变量）；LeetCode 304；→ 错题本 #9、#10

#### Q8 · 滑动窗口里有嵌套的 `while`，为什么复杂度是加法 O(n) 而不是乘法 O(n²)？
- **时间**：2026-11-07 11:54
- **原始问题**：先问「滑动窗口比起用二重循环枚举所有子串，能快多少？用 O 怎么表示？」。我解释了「`right` 走 n 步 + `left` 最多走 n 步 = O(2n) = O(n)」之后，追问：「为什么是加法呢，那也是乘法吧」。
- **卡点**：看到循环里套循环，就默认是「外层次数 × 内层次数」。
- **讲解过程**：
  1. **复杂度对比**：567 暴力枚举每个长度为 k 的子串再比较 → O(n·k)；滑动窗口 → O(n + k)。76 暴力枚举所有子串 → O(n²)～O(n³)；滑动窗口 → O(n + m)。
  2. **乘法什么时候成立**：内层循环的变量**每次进入都被重置**。
     ```python
     for i in range(n):
         for j in range(n):   # 每一轮外层，j 都重新从 0 开始
     ```
     n + n + … + n（n 个）= n × n。**乘法就是「每一轮都一样多」时的加法。**
  3. **滑动窗口为什么是加法**：`left = 0` 只在最外面初始化一次，之后**只往右走，从不回退、从不重置**。每一轮内层走几步不一样，但加起来最多 n 步。
     | 外层第几轮 | 1 | 2 | 3 | 4 | 5 | 6 |
     |---|---|---|---|---|---|---|
     | 内层执行次数 | 0 | 0 | 2 | 0 | 1 | 3 |
     合计 6 = n。某一轮多走了，别的轮次就少走了：`left` 一辈子只有 n 步的「预算」。
  4. **比喻**：走廊 n 块地砖。每走一块就回到起点重走一遍 → n²；走走停停但从不回头 → n。
  5. 这种分析叫**均摊分析**：不看单独一轮最多几步，而是看**整个运行过程**里内层一共执行了多少次。单调栈的 `pop` 也是同理（每个元素最多入栈一次、出栈一次）。
- **结论**：判断嵌套循环的复杂度，先问「**内层的变量每次会不会被重置？**」。会重置 → 一般是乘法；不重置并且只朝一个方向走 → 把总步数加起来，往往是 O(n)。
- **待办**：检验题还没回答：`j = 0` 写在 `for i` 外面，`while j < n and nums[j] < nums[i] + 10: j += 1`，总复杂度是多少？
- **关联**：LeetCode 76、567（滑动窗口）、单调栈；→ Q9（26 题的快慢指针也是同一类）、Q11（3Sum 的双指针）

#### Q9 · LeetCode 26 删除有序数组中的重复项：`fast += 1` 能挪到循环最前面吗？
- **时间**：2026-11-07 11:54
- **原始问题**：快慢指针的标准写法里，`fast += 1` 写在 `while` 循环体的最后。「我能把 `fast += 1` 写在 `while fast < len(nums):` 下面吗？」「如果那么写的话，整体代码应该怎么改？」
  ```python
  slow = fast = 0
  while fast < len(nums):
      if nums[fast] != nums[slow]:
          slow += 1
          nums[slow] = nums[fast]
      fast += 1
  return slow + 1
  ```
- **卡点**：只挪 `fast += 1` 这一行，下面还是读 `nums[fast]`。
- **讲解过程**：
  1. 用 `[1, 1, 2]` 跟踪：进入循环时 `fast = 2`，满足 `2 < 3`，`+= 1` 后变成 3，读 `nums[3]` → **`IndexError`**。（顺带第一轮 `nums[0]` 也没读到，不过它本来就等于 `nums[slow]`。）
  2. **改法**：`fast` 加完 1 之后，凡是读 `nums[fast]` 的地方都改成 `nums[fast - 1]`：
     ```python
     while fast < len(nums):
         fast += 1
         if nums[fast - 1] != nums[slow]:
             slow += 1
             nums[slow] = nums[fast - 1]
     return slow + 1
     ```
     实际读到的下标是 0、1、2，不多也不少。
  3. **两种写法 = 两种含义**：
     | | `+= 1` 放在最后 | `+= 1` 放在最前 |
     |---|---|---|
     | `fast` 的含义 | 当前**正在处理**的下标 | 已经**处理过**几个元素 |
     | 读元素 | `nums[fast]` | `nums[fast - 1]` |
     滑动窗口里 `right += 1; c = s2[right - 1]` 用的就是「放最前」的写法，好处是窗口 `[left, right)` 左闭右开，长度直接是 `right - left`。
- **结论**：两种都对，关键是**一段代码里指针只有一种含义**。挪了 `+= 1`，所有用到这个指针的地方都要跟着改。
- **待办**：检验题：用「放最前」的写法又不想写 `fast - 1`，`fast` 的初始值和 `while` 条件要怎么改？（提示：`fast = -1`）
- **关联**：Q8；滑动窗口 76、567 的 `right - 1`；off-by-one（错题本 #4）

#### Q10 · LeetCode 5 最长回文子串：中心扩展法里 `length = right - left - 1` 为什么要减 1？
- **时间**：2026-11-07 11:54
- **原始问题**：看了一份 Java 题解（中心扩展法，奇数中心 `(i, i)`、偶数中心 `(i, i+1)`），问「这里的 `length` 为什么还要减 1？」
  ```java
  while (left >= 0 && right < s.length() && s.charAt(left) == s.charAt(right)) {
      left--; right++;
  }
  int length = right - left - 1;
  if (length > maxLength) { maxLength = length; start = left + 1; }
  ```
- **卡点**：不清楚 `while` 退出时 `left` 和 `right` 指在哪里。
- **讲解过程**：
  1. 用 `s = "xabay"`、中心 `i = 2` 跟踪：`(2,2)` b==b → `(1,3)` a==a → `(0,4)` x≠y **退出**。
     ```
     下标:   0   1   2   3   4
     字符:   x   a   b   a   y
             ↑   └─ 回文 ─┘   ↑
            left             right
     ```
  2. 退出时两个指针都**多走了一步**，停在回文外面的「失败位置」上。真正的回文是闭区间 `[left+1, right-1]`。
  3. 闭区间 `[a, b]` 的长度是 `b - a + 1` → `(right-1) - (left+1) + 1 = right - left - 1`。验证：`4 - 0 - 1 = 3`（aba）✅
  4. 同理 `start = left + 1`：回文的起点在 `left` 右边一格。
- **结论**：循环退出时，`left`、`right` 停在回文**外面**两端；夹在中间、不含两端的部分才是回文，所以长度 = `right - left - 1`。**先想清楚指针停下时指在哪里，`±1` 就能自己推出来。**
- **待办**：检验题：`s = "ab"`、`i = 0` 的偶数中心，循环一次都不执行，`length` 等于多少？合理吗？（答案应该是 0：空回文）
- **关联**：Q9（指针停在哪里）；区间长度公式；off-by-one（错题本 #4）

#### Q11 · LeetCode 15 三数之和：超出内存限制、漏答案、跳过重复元素的几种写法
- **时间**：2026-11-07 11:54
- **原始问题**：用「排序 + 固定一个数 + `twoSumTarget` 双指针」写 3Sum，提交后在 `[-1,0,1,2,-1,-4]` 上**超出内存限制**，问「有什么问题吗？」。修了一版又问「这样子？」，然后问「按原来 `nums[left] == nums[left+1]` 的写法能不能行」，最后问「为了提高效率，想在其他分支里也跳过重复值，应该怎么改？」
- **卡点**（按版本）：
  1. **第一版**：`elif sum < target` 和 `if` 的条件一样；`else` 里记录答案后 `left`、`right` 可能原地不动；`res.append([left, right])` 记的是下标；外层 `nums[i+1]` 在 `i = n-1` 时越界。→ 错题本 #11
  2. **第二版**：改成 `low, high` 记住旧值来跳重复（对的），但在 `if/elif/else` **外面**又加了 `left += 1; right -= 1` → `[-1,0,1]`、`[-2,1,1]` 被漏掉。→ 错题本 #12
  3. **原写法**：`if` 分支里「先 `left += 1`，再 `while nums[left] == nums[left+1]`」→ `[-2,0,1,1]` 返回 `[]`。→ 错题本 #13
- **讲解过程**：
  1. **读报错**：超出内存限制 ≈ 有个死循环在不停地 `append`。找「哪个循环出不去 + 哪里在一直加东西」。第一版里 `sum > target` 掉进 `else`，指针不动，同一组答案被无限追加。
  2. **两种「跳重复」的 `while` 停的位置不同**：
     ```
     nums:  1  1  1  5
     while nums[left] == nums[left+1]  → 停在最后一个 1（还没离开这个值，之后要再 +1）
     while nums[left] == low           → 停在 5（已经是新值，不用再 +1）
     ```
  3. **为什么「先走一步再跳」会出错**：走一步之后已经落在**新值**上，再跳就把新值的重复串也跳过去了。`[-2,0,1,1]` 里，`left` 从 0 走到第一个 1，再被推到 `right` 的位置，错过了 `1 + 1 = 2`。
  4. **最简单的正确写法**：只在 `else` 里去重，`if/elif` 只走一步。重复答案只会在「找到答案之后」产生，没找到时多比较一次也不会多记结果。
  5. **想在所有分支都跳重复（两种都对，对拍了 2 万组随机数据）**：
     ```python
     # 写法一（推荐）：记住旧值，一直走到值变了为止
     while left < right:
         low, high = nums[left], nums[right]
         total = low + high
         if total < target:
             while left < right and nums[left] == low: left += 1
         elif total > target:
             while left < right and nums[right] == high: right -= 1
         else:
             res.append([low, high])
             while left < right and nums[left] == low: left += 1
             while left < right and nums[right] == high: right -= 1

     # 写法二：和下一个比，但「先跳过重复串，再走一步」
     if total < target:
         while left < right and nums[left] == nums[left+1]: left += 1
         left += 1
     ```
  6. **为什么 `if` 分支里整串跳过是安全的**：`total < target` 说明 `low` 加上目前**最大的** `nums[right]` 都不够，`low` 和剩下的谁配都不够，所有等于 `low` 的位置都可以扔掉。
  7. **效率**：跳不跳重复都**不改变复杂度**，`twoSumTarget` 是 O(n)（Q8 的均摊分析），3Sum 整体 O(n²)，只是少做几次比较。选最不容易写错的写法就行。
- **结论**：跳重复的关键是「**跳完以后指针要停在一个新值上**」；指针的移动要写在**各自分支里面**，不要写在分支外面让所有分支都多走一步。
- **待办**：① 检验题：写法一里 `low, high = ...` 为什么必须写在 `while` 循环**里面**？② 修好后提交到 LeetCode。③ `threeSumTarget` 的 `start` 参数没用上（应写 `i = start`）；`sum`、`tuple` 覆盖了内置函数名，改成 `total`、`pair`。
- **关联**：Q8（复杂度）、Q9（指针停在哪里）；LeetCode 1（两数之和）、18（四数之和）；→ 错题本 #11、#12、#13

#### Q12 · LeetCode 724 寻找数组的中心下标：前缀和版本的 4 个 bug
- **时间**：2026-11-02 09:00
- **原始问题**：贴了自己的代码和报错 `AttributeError: 'Solution' object has no attribute 'preSum'`（没写问题文字）。
  ```python
  class Solution:
      def pivotIndex(self, nums):
          sum = Sum(nums)
          index = sum.findIndex(nums, self.preSum)
          return index

  class Sum:
      def __init__(self, nums):
          n = len(nums)
          init = 0
          self.preSum = [0]*(1+n)
          for i in range(1, n+1):
              init += nums[i-1]
              self.preSum[i] = init

      def findIndex(self, nums, preSum):
          for i in range(1, n+1):
              if preSum[i]-nums[i-1] == preSum[n+1]-preSum[i]:
                  return i
          return -1
  ```
- **卡点**：思路对（左边和 = `preSum[i] - nums[i-1]` = `preSum[i-1]`，右边和 = 总和 − `preSum[i]`），但写成代码时出了 4 个 bug。
- **讲解过程**：
  1. **Bug 1（报错本身）**：`pivotIndex` 里的 `self` 是 `Solution` 对象，`preSum` 挂在 `Sum` 对象上 → 应该通过 `sum.preSum` 拿。而且 `findIndex` 本身就是 `Sum` 的方法，自己就能用 `self.preSum`，不需要再当参数传。
  2. **Bug 2**：`findIndex` 里的 `n` 是 `__init__` 的**局部变量**，在别的方法里看不到（Q6）→ 用 `len(nums)` 或存成 `self.n`。
  3. **Bug 3**：`preSum` 长度是 `n+1`，合法下标是 `0..n` → `preSum[n+1]` 越界，总和应该是 `preSum[n]`。
  4. **Bug 4**：`i` 是 `preSum` 的下标，比 `nums` 的下标大 1 → 应 `return i - 1`。
  5. **风格**：`sum = Sum(nums)` 盖住了内置函数 `sum`（Q5）→ 改成 `prefix`。
- **结论**：属性挂在哪个对象上，就要通过哪个对象去拿；局部变量出了函数就没了；`preSum` 比原数组多一位，下标换算要 ±1。
- **待办**：检验题（来自 Q18）：`preSum[0] = 0` 这个哨兵消除了哪种特殊情况？
- **关联**：Q1（`self`）、Q5、Q6、Q7（前缀和）；→ 错题本 #15

#### Q13 · LeetCode 370 区间加法（差分数组）：二维列表怎么遍历、方法怎么调用
- **时间**：2026-11-03 03:53
- **原始问题**：写了 `Difference` 类（`__init__` 建差分数组、`increment(i, j, val)`、`result()`、`multiIncrement(operations)`），说「我对最后一个有问题」：
  ```python
  def multiIncrement(self, operations: list(list[int])) -> None:
      # 如何将二维数组遍历，每一行的列表中的各个元素都能提取
      for i in operations:
          increment(self.diff, i[0], i[1], i[2])
  ```
- **卡点**：不确定怎么遍历二维列表；调用自己类的方法时漏了 `self.`，还手动传了 `self.diff`。
- **讲解过程**：
  1. `for i in operations` 每次拿到**一整行**，`i[0]`、`i[1]`、`i[2]` 能用 ✅。改进：名字叫 `op`；或者直接解包 `for start, end, val in operations:`（→ Q14）。
  2. **调用方法**：`increment` 是方法，要写 `self.increment(...)`（错题本 #6）；`self` 会自动传进去（bound method，Q1），`self.diff` 方法自己就能拿到，不用传：
     ```python
     for start, end, val in operations:
         self.increment(start, end, val)
     # 或者
     for op in operations:
         self.increment(*op)
     ```
  3. **类型注解**：`list(list[int])` 用了圆括号 → 实际试过不会报错（会被算成某个奇怪的值），但不是有效注解，应写 `list[list[int]]`。
  4. **`Solution` 里没问到的 bug**：`difference.multiIncrement` 和 `difference.result` 都没加 `()`，只是拿到了 bound method 对象，**根本没调用**；`multiIncrement` 还需要传 `operations`。
- **结论**：遍历二维列表直接 `for row in rows`，固定长度就解包；方法要通过对象调用并且加 `()`。
- **关联**：Q1（bound method）、Q14（解包）；→ 错题本 #6、#16

#### Q15 · LeetCode 151 反转字符串中的单词：`split`、`join`、倒序、边遍历边删除
- **时间**：2026-11-03 05:01 ~ 07:23（中间连续问了很多语法问题）
- **原始问题**：截图里的代码思路是 split → 倒序 → join，有一个 `cleanSpaces` 想删掉多余的空格。依次问了：
  1. 「不传参数默认是怎么 split 的？」
  2. （边遍历边删除那道题）「应该不会，只删除了第一个。那我应该怎么办？」
  3. 「`a[:]` 为什么是浅拷贝？`[v for v in a if v != '']` 是什么语法，为什么要写 `in a`？」
  4. （截图 `AttributeError: 'list' object has no attribute 'join'`）
  5. 「`reverse` 在 Python 中怎么用？」
  6. 「可以创造一个什么都没有的空列表吗？」
  7. 「`range` 可以从大到小吗？」
- **卡点**：`split(',')` 分隔符写错；以为 `split(" ")` 会留下 `' '`；`pop(str_list[index])` 不通过对象调用、而且传的是元素；`list.join`；切片 `[-1:0:-1]` 漏了下标 0；`[''] * len` 占位后有空位留下。
- **讲解过程**：
  1. **`split()` 不传参数**：任意空白都算分隔符；连续空白只切一刀；开头结尾的空白丢掉 → **结果里永远没有 `''`**。
     ```python
     "  hello  world  ".split(" ")   # ['', '', 'hello', '', 'world', '', '']
     "  hello  world  ".split()      # ['hello', 'world']
     "   ".split()  → []      "".split(" ") → ['']
     ```
     多余空格变成的是 `''`（空字符串），不是 `' '` → `if obj == ' '` 永远匹配不到。有了 `split()`，`cleanSpaces` 可以整个删掉。
  2. **边遍历边删除**：`['x', '', '', 'y']` 用 `enumerate` + `pop(i)` 只删掉第一个 `''`（用户猜对了）。删除让后面的元素往前挪，下标照样往后走 → 跳过一个。三种解决办法：
     - 造新列表：`a = [v for v in a if v != '']`（推荐）
     - 从后往前删：`for i in range(len(a)-1, -1, -1): ...`（后面的已经检查过了，前面的下标不变）
     - 遍历副本：`for v in a[:]: a.remove(v)`（慢）
     > 规则：不要在遍历一个列表的同时改变它的长度。
  3. **`a[:]` 是浅拷贝**：切片会造新列表，省略开始和结束 = 整个列表。只复制最外层，里面的元素还是原来的对象（`b[0] is a[0]` 为 True）。等价写法：`list(a)`、`a.copy()`、`copy.copy(a)`；深拷贝 `copy.deepcopy(a)`。
  4. **列表推导式**：
     ```
     [  v      for v in a      if v != ''  ]
       放什么    从哪里拿          要哪些（可选）
     ```
     等价于 `result = []; for v in a: if v != '': result.append(v)`。`in a` 就是「从哪里拿元素」。`a = [...]` 是把名字 `a` 挪到新列表上，原列表没被修改。
  5. **`join` 是字符串的方法**：`" ".join(列表)`，粘合剂是主语。
  6. **切片 `[-1:0:-1]`**：结束下标不包含 → 漏掉 `'the'`；预先 `[''] * 4` 只填了 3 个，剩一个 `''`，`join` 后末尾多一个空格。整个倒过来用 `[::-1]`。
  7. **三种倒序**：
     | 写法 | 改原列表？ | 返回 | 字符串能用？ |
     |---|---|---|---|
     | `a.reverse()` | ✅ | `None` | ❌ |
     | `reversed(a)` | ❌ | 迭代器 | ✅ |
     | `a[::-1]` | ❌ | 新列表 / 新字符串 | ✅ |
     > 原地修改的方法（`reverse`、`sort`、`append`）都返回 `None` → `" ".join(words.reverse())` 会报错。
  8. **空列表**：`[]` 或 `list()`，用 `append` 放元素，「放了几个就有几个」；和 `[''] * n`（一开始就有 n 个元素）不同。
  9. **`range` 从大到小**：`range(开始, 结束, 负步长)`，结束仍不包含 → 要包含 0 得写 `range(n-1, -1, -1)`；忘了负步长 `range(5, 0)` → 空，不报错。
- **结论**：151 一行就够：`return " ".join(s.split()[::-1])`（或 `reversed(s.split())`）。
- **待办**：① 自己写出这一行并提交；② 检验题：`a = ['x','','y']; b = a; a = [v for v in a if v != '']; print(a, b)`；③ `range(len(words)-1, 0, -1)` 会漏掉谁？
- **关联**：错题本 #1/#2（名字标签）、#3（共享引用）、#4（off-by-one）、#9（`None`）；→ 错题本 #17、#18、#19

#### Q16 · LeetCode 54 螺旋矩阵：超出时间限制；判断列表是否为空
- **时间**：2026-11-03 07:27 ~ 08:08
- **原始问题**：截图，提交后「超出时间限制」。之后问「Python 有没有判断 list 是不是 empty 的函数？」
- **卡点**：四个方向前面的 `if` 条件，比较方向写反了，而且用了 `<` 而不是 `<=`。
- **讲解过程**：
  1. **超时 ≠ 太慢**：`while len(output) < m*n` 一直成立，说明 `output` 不再变长 → 死循环。本地限制 50 轮跑示例 1，`output` 停在 `[3, 6, 9, 7, 4, 1]`。
  2. **推演第一轮**（`upper=0, lower=2, left=0, right=2`）：上边写的是 `if lower_bound < upper_bound` → `2 < 0` 为 False，第一行整个被跳过。
  3. **第二轮**只剩中间一列（`left = right = 1`）：`if left_bound < right_bound` → `1 < 1` 为 False，但这一列还要走。
  4. **规则**：每个 `if` 的意思都是「**这条边上还有没走过的格子吗**」→ 上/下边：`upper <= lower`；右/左边：`left <= right`。边界相等时还剩一行 / 一列。
  5. 改好后用非正方形矩阵（3×4）再测一遍（错题本 #10 的经验）。本地验证过修好的条件，3×3 和 3×4 都正确。
  6. **判断空列表**：没有专门的函数，推荐 `if not a:`（PEP 8 推荐）；也可以 `len(a) == 0`。
     | 算作 `False` | 算作 `True` |
     |---|---|
     | `[]` `()` `{}` `set()` `""` `0` `0.0` `None` | 只要有内容：`[0]`、`[""]`、`" "` |
     坑：`[0]`、`[""]` 不是空的；`None` 也算 False，要区分时写 `if a is None:`。
     `if not matrix or not matrix[0]: return []`：`or` 短路，空列表时不会去读 `matrix[0]`。
- **结论**：超时先怀疑死循环；边界条件要用一句话说清楚它的意思再写成代码，相等的情况往往是最容易漏的。
- **待办**：把修好的版本提交。
- **关联**：错题本 #4（off-by-one）、#10（非正方形测试）；→ 错题本 #20

#### Q17 · 单调栈（下一个更大元素）：`s` 是干什么的？`while s and s[-1] <= nums[i]` 是什么意思？
- **时间**：2026-11-03 08:33 ~ 08:44
- **原始问题**：贴了一张「找身后第一个比自己高的人」的比喻图和代码，说「我看不懂他说的和这个代码有什么关系」，然后「还是没懂，`s` 是干什么的？`while s and s[-1] <= nums[i]` 是啥意思，你一步一步慢慢讲」。
  ```python
  def calculateGreaterElement(nums):
      n = len(nums)
      res = [0]*n
      s = []
      for i in range(n-1, -1, -1):
          while s and s[-1] <= nums[i]:
              s.pop()
          res[i] = -1 if not s else s[-1]
          s.append(nums[i])
      return res
  ```
- **卡点**：不知道栈是什么；看不出比喻和代码的对应关系。
- **讲解过程**：
  1. **栈**：一个普通列表，只动末尾：`append` 放、`s[-1]` 看、`pop()` 拿。像一摞盘子。
  2. **`s` 的定义**：从当前位置往右看，**有可能挡住视线的人**（候选答案名单）。从底到顶越来越矮 → 「单调」栈。
  3. **比喻 ↔ 代码**：
     | 比喻 | 代码 |
     |---|---|
     | 看「后面」的人 | 从右往左 `range(n-1, -1, -1)`，先处理右边 |
     | 比我矮的都被我挡住了 | `while s and s[-1] <= nums[i]: s.pop()` |
     | 第一个露出来的就是答案 | `res[i] = s[-1]`（栈空就是 -1） |
     | 我也站进队伍 | `s.append(nums[i])` |
  4. **拆 `while`**：「只要名单里还有人（`s`），**并且**最上面那个人不比我高，就划掉他」。划掉是安全的：他不是我的答案，对我左边的人来说他也被我挡住了。`s and` 先判断非空，`and` 短路，不会对空列表读 `s[-1]`。
  5. **跟踪 `[2, 1, 2, 4, 3]`**：
     | `i` | `nums[i]` | 弹出 | `res[i]` | 放入后 `s` |
     |---|---|---|---|---|
     | 4 | 3 | — | -1 | `[3]` |
     | 3 | 4 | 3 | -1 | `[4]` |
     | 2 | 2 | — | 4 | `[4, 2]` |
     | 1 | 1 | — | 2 | `[4, 2, 1]` |
     | 0 | 2 | 1、2 | 4 | `[4, 2]` |
  6. **复杂度**：每个元素最多入栈、出栈各一次 → O(n)（暴力 O(n²)）。
- **结论**：单调栈 = 维护一份「还有可能成为答案」的名单，不可能的立刻扔掉。
- **待办**：① 自己写出 `i = 1`、`i = 0` 两步；② 把 `<=` 改成 `<`，`res[0]` 会变成多少？
- **关联**：Q8（均摊分析）、Q16（判断空列表、`and` 短路）、Q18

#### Q18 · 「代入法」：题解是怎么把第一轮和后面的轮合并成一套流程的？
- **时间**：2026-11-03 09:49 ~ 09:56
- **原始问题**：「有的时候需要注意第一轮和后面所有轮的情况不一样，我发现有的题解涵盖了第一轮和后面轮的所有情况，好奇他们是怎么想的。就拿刚才这个单调栈代码为例。」追问：「我就是不知道怎么想到这个的，按照一轮和二轮的角度，我会想到需要分开，但不知道怎么合并成同一套流程。」
- **卡点**：能想到分情况，但不知道怎么合并。
- **讲解过程**：
  1. **按「情况」分，而不是按「第几轮」分**：单调栈第一轮特殊是因为「栈空」，而栈空在后面（`i = 3`）也会出现 → 同一种情况。
  2. **先定义状态的意思，初始值就推出来了**：`s` = 右边可能挡住视线的人 → 还没处理任何人时 → `[]`。
  3. **代入法四步**：
     1. 老老实实把第一轮和后面的轮分开写；
     2. 并排比较，找出不同（单调栈只有两处：有没有 `while`、答案是 `-1` 还是 `s[-1]`）；
     3. **把第一轮的状态代进通用代码，一行一行跑，看哪一行出错，问自己「我希望这一行在这种状态下做什么？」，只修那一行**：`while s[-1] <= ...` 空栈报错 → 改成 `while s and ...`（执行 0 次）；`res[i] = s[-1]` 报错 → 改成 `-1 if not s else s[-1]`；
     4. 再代入检查一遍，结果和特殊分支完全一样 → 删掉特殊分支。顺便还处理了「后面某一轮栈被弹空」这个分开写时容易漏的情况。
  4. **练习**：`best = None` + `if i == 0: best = x else: best = max(best, x)` → 用户答出 `best = -INF` ✅（Python 写 `float('-inf')` 或 `-math.inf`）。
  5. **中性初始值**：求和 `0`、求积 `1`、最大值 `-inf`、最小值 `inf`、收集 `[]`；前缀和多加的一行一列 0 叫**哨兵**（sentinel）。
  6. 别忘了把**空输入**也代进去试（空列表时返回 `-inf` 对不对要看题目）。
- **结论**：不要问「怎么合并两段代码」，而要问「**把特殊情况的状态代进通用代码，哪一行出错？我希望它做什么？**」，然后用中性初始值 / 哨兵 / 短路条件让通用代码自然地做对。
- **关联**：Q7（前缀和哨兵）、Q12（724 的 `preSum[0]`）、Q17、Q19（`get(c, 0)`、`defaultdict`）

#### Q20 · LeetCode 76 最小覆盖子串：`start` 记错、`valid` 什么时候减 1
- **时间**：2026-11-05 15:42 ~ 15:45
- **原始问题**：截图「有什么问题」，改了一版后再贴代码。
  ```python
  while valid == len(need):
      if right - left < length:
          length = right - left
          start = left          # 第一版写的是 start = right
      d = s[left]
      left += 1
      if d in need:
          window[d] -= 1
          valid -= 1            # 无条件减 1
  return '' if length == float('inf') else s[start:start+length]
  ```
- **卡点**：`start` 记成了 `right`；收缩时每移出一个需要的字符都 `valid -= 1`。
- **讲解过程**：
  1. **窗口定义**：先 `right += 1` 再取 `s[right-1]` → 窗口是 `[left, right)`，长度 `right - left`，起点是 `left` → `start = left`。
  2. **找不到时**：`length` 一直是 `inf` → 返回 `''`（第二版改对了）。
  3. **`valid` 的意思**：有多少种字符的数量**已经够了**。加入时只在 `window[c]` **刚好从不够变成够**（`==`）时 +1；移出时也只能在**刚好从够变成不够**时 -1：
     ```python
     if d in need:
         if window[d] == need[d]:   # 移出前刚好够 → 移出后就不够了
             valid -= 1
         window[d] -= 1             # 判断要放在 -= 1 前面
     ```
  4. **本地验证**：用户的版本 `"ADOBECODEBANC"/"ABC"` → `"ADOBEC"`（应为 `"BANC"`），`"AAB"/"AB"` → `"AAB"`（应为 `"AB"`）。跟踪 `"AAB"`：移出第一个 A 后窗口 `"AB"` 里 A 还够，却减了 `valid` → 提前停止收缩，错过更短的答案。
- **结论**：计数器只在**状态刚好跨过界限**的那一刻变化，加入和移出是对称的。
- **待办**：改好后提交。（567 里用户已经写对了这一段，说明想通了。）
- **关联**：Q8（复杂度）、Q19（`get`）、Q21；→ 错题本 #21

#### Q21 · LeetCode 567 字符串的排列：窗口大小用错了长度
- **时间**：2026-11-06 03:27 ~ 03:43
- **原始问题**：截图「有什么问题呢」，失败用例 `s1 = "abcdxabcde"`、`s2 = "abcdeabcdx"`，预期 `true`，输出 `false`。
- **卡点**：`if right - left == len(need):` 用 `len(need)` 当窗口大小。
- **讲解过程**：
  1. 第一张截图里有 `if ... = ...`（应为 `==`，会 `SyntaxError`），第二版已改。
  2. 收缩时先判断 `window[d] == need[d]` 再 `-= 1` ✅（76 的 bug 在这里写对了）。
  3. `len(s1) = 10`，`len(need) = 5`（不同字符 a、b、c、d、x，重复的只算一个 key）。前面的用例通过，是因为 s1 里没有重复字符时两者恰好相等。
     | 行 | 意思 | 应该用 |
     |---|---|---|
     | 窗口大小判断 | 窗口长度 = 排列的长度 | `len(s1)` |
     | `valid` 判断 | 每**种**字符的数量都够了 | `len(need)` |
  4. `start`、`length` 是从 76 带过来的，这题用不上，可删。
- **结论**：`len(need)` 是「字符的**种数**」，`len(s1)` 是「字符的**个数**」；测试时要用有重复字符的输入。
- **关联**：Q19、Q20；→ 错题本 #22

#### Q22 · 3Sum 外层循环：为什么用 `for` 是错的，用 `while` 是对的？
- **时间**：2026-11-07 12:00
- **原始问题**：「这两个有什么区别，我用 `for` 是错误的，用 `while` 是正确的」
  ```python
  for i in range(len(nums)):
      ...                                   # 调用 twoSumTarget，收集结果
      while i < n-1 and nums[i] == nums[i+1]:
          i += 1                            # 想在这里跳过重复的 nums[i]
  ```
- **卡点**：以为在 `for` 循环体里改 `i`，下一轮会从改过的位置继续。
- **讲解过程**：
  1. 实验：`for i in range(5): i += 10` → 每轮拿到的还是 0、1、2、3、4。
  2. **原因（名字标签）**：`range` 自己记着进度；每一轮开始，`for` 把**下一个值**重新贴到名字 `i` 上。循环体里 `i += 1` 只是把标签挪走，`range` 的进度完全不受影响 → 跳重复的效果被抹掉 → 重复答案（`[-4,-1,-1,0,1,2]` 里第二个 `-1` 又找出一次 `[-1,0,1]`）。
  3. `while` 里 `i` 只由自己控制，跳过就是真的跳过。
  4. **`for` 也能去重的写法**（4Sum 里用户自己写出来了）：
     | 写法 | 思路 | 能用在 `for` 里吗？ |
     |---|---|---|
     | `while nums[i] == nums[i+1]: i += 1` | 往后看，自己把 `i` 推过重复串 | ❌ 下一轮被 `range` 重设 |
     | `if i > start and nums[i] == nums[i-1]: continue` | 往前看，和上一个一样就跳过这一轮 | ✅ 不改 `i` |
- **结论**：`for` 的循环变量每轮都会被重新赋值，在循环体里改它没用；要自己控制下标就用 `while`，或者改成「和前一个比 + `continue`」。
- **待办**：预测题：`for` 版本在 `i = 2` 那一轮会多找出哪一组？（应为又一组 `[-1, 0, 1]`）
- **关联**：错题本 #1/#2（名字标签）；Q11；→ 错题本 #23

#### Q23 · LeetCode 18 四数之和：复用 3Sum 的函数，输出一大堆重复和错误的组合
- **时间**：2026-11-07 12:10
- **原始问题**：截图 + 代码「这有什么问题」。`fourSum` 固定一个数调用 `threeSumTarget`，`threeSumTarget` 再调用 `twoSumTarget`。Example 1 输出了 12 组，比如 `[0, 2, -1, -1]`。
- **卡点**：
  1. `threeSumTarget` 里 `i = 0`，没用参数 `start`（3Sum 时我列为「小问题」，因为外层传的正好是 0；4Sum 传 `i+1` 就出错了）。
  2. `fourSum` 里跳重复的 `while` 写在调用 `threeSumTarget` **之前**。
  3. 类型注解 `target: long`。
- **讲解过程**：
  1. 本地复现，输出和截图一模一样。`[0, 2, -1, -1]`：数组里只有一个 `-1` 却用了两次 → 内层每次从 0 开始找，已用过的元素被重复使用，同一组换个顺序也被找出来。→ 改 `i = start`。
  2. 修好后 Example 2 `[2,2,2,2,2]` 返回 `[]`：先跳重复，`i` 直接到下标 4，后面没元素了 → 必须**先处理、再跳重复**（和错题本 #13 同一个道理）。
  3. Python 没有 `long`，`int` 任意大不溢出；`long` 是 Java / C++ 的写法（错题本 #8 同类）。
  4. 两处都修后，两个示例都正确。
- **结论**：被复用的函数，参数一定要真的用上（「碰巧传 0」会掩盖 bug）；去重要在处理完当前元素**之后**。
- **关联**：Q11、Q22；→ 错题本 #24、#25

#### Q24 · nSum 递归：漏了排序；`continue` 放在递归之前；「自己调用自己」叫什么？
- **时间**：2026-11-07 12:30
- **原始问题**：把 4Sum 改成通用的 `nSumTarget(nums, target, start, n)`（`n == 2` 双指针，否则 `for i in range(start, sz)` 固定一个数再递归 `n-1`），贴了代码（没写问题）。之后：「你是说先 `continue`，我觉得可以」「我的这个解法就不需要写多个函数来互相引用了，这样子的自己套用自己的叫什么？」
- **卡点**：整个程序里没有 `nums.sort()`；`if i > start and nums[i] == nums[i-1]: continue` 放在递归调用之后。
- **讲解过程**：
  1. 本地跑：`[1,0,-1,0,-2,2]` → 只有 `[[-2, 2, 0, 0]]`。双指针「`sum < target` 就让 `left` 右移」和「和前一个比去重」都要求数组**有序**。`sort()` 加在 `fourSum` 里（只排一次），不要加在递归函数里（会被调用很多次）。加上后随机对拍 5000 组全对。
  2. **先 `continue` 再递归**：结果不变，省下一整次递归（这一层本身就是 O(n²)）。规律：能提前排除的情况，就在昂贵计算之前排除。
  3. **递归**：函数调用自己。必须有两部分：
     | 部分 | 代码 | 作用 |
     |---|---|---|
     | 基本情况 | `if n == 2:` 双指针 | 直接解决，不再调用自己 |
     | 递归情况 | `self.nSumTarget(..., i+1, n-1)` | 把问题变小，交给自己 |
     `n=4 → n=3 → n=2` 停下。
  4. **思考方式**：不去展开整个调用过程，而是「**信任**函数对 `n-1` 能给出正确答案」，只考虑这一层：固定 `nums[i]`，把小问题交出去，拿回结果加上 `nums[i]`。
  5. `if sz < n or n < 2: return res` 是保险：保证 `n` 不会一路减成负数、永远到不了基本情况（否则 `RecursionError`）。
  6. `i > start`（而不是 `i > 0`）保证每一层只和**本层**处理过的元素比较。
- **结论**：几个长得几乎一样、只差一个规模的函数 → 提取成一个递归函数；写递归 = 想清楚基本情况 + 信任递归处理好更小的问题。
- **待办**：① 检验题：`i > start` 写成 `i > 0`，`[2,2,2,2,2]`、`target = 8` 会得到什么？② 用 `nSumTarget` 两行写出 `threeSum`。
- **关联**：Q18（代入法：先想通用的一步，再查最小情况）、Q22、Q23；→ 错题本 #26

#### Q25 · LeetCode 42 接雨水：暴力解法哪里有问题
- **时间**：2026-11-07 13:00
- **原始问题**：截图「哪里有问题」，两个示例都通过了。
  ```python
  for i in range(1, n-1):
      l_max, r_max = 0, 0
      for l in range(i):        # 左边最高（不含 i）
          ...
      for r in range(i+1, n):   # 右边最高（不含 i）
          ...
      res += min(l_max, r_max) - height[i]
  ```
- **卡点**：`l_max`、`r_max` 都没包含 `i` 自己；O(n²)。
- **讲解过程**：
  1. 思路正确：每个位置的水 = `min(左边最高, 右边最高) − 自己的高度`。
  2. **负数**：`[1, 2, 1]` → `i = 1` 时 `min(1, 1) - 2 = -1`，正确答案是 0。改法：只加正数；或者让范围包含 `i` 自己（`range(i+1)`、`range(i, n)`），这样 `min` ≥ `height[i]`，结果永远 ≥ 0。
  3. **超时**：n 最大 2×10⁴，n² = 4×10⁸。`l_max(i) = max(l_max(i-1), height[i])`，和前缀和一样每项由前一项 O(1) 推出 → 先从左往右算出所有 `l_max`，从右往左算出所有 `r_max`，再扫一遍 → O(n)。
- **结论**：「示例都过了」不代表对，要自己构造极端小例子（中间最高）；重复扫描的「左边最大值」可以像前缀和一样预处理。
- **待办**：① 回答 `[1, 2, 1]` 算出多少；② 写出预处理 `l_max` / `r_max` 数组的 O(n) 版本并提交。
- **关联**：Q7、Q12（前缀和思想）；→ 错题本 #27

#### Q26 · 二分查找左边界：为什么 `==` 时 `right = mid - 1`？为什么返回 `left`？什么时候会越界？
- **时间**：2026-11-07 13:20 ~ 14:30
- **原始问题**：
  ```python
  def left_bound(nums, target):
      left, right = 0, len(nums) - 1
      while left <= right:
          mid = left + (right - left) // 2
          if nums[mid] < target:   left = mid + 1
          elif nums[mid] > target: right = mid - 1
          elif nums[mid] == target: right = mid - 1   # 收缩右侧边界
      return left
  ```
  「这个算法竟然能找到左边界，我觉得不可思议。为什么 `==` 时要 `right = mid - 1`？我本来觉得如果第一次算出来的 `mid` 就是左边界，会导致搜索失败，但我自己一步一步写了一下，竟然能找到，只是多走几步。」之后追问：「什么情况下会越界？」「只是查找一个数字也可能越界吗？」「我说的是最后的 `left` 也可能超出范围，只是 `return -1` 让我们避免了检查」「为什么返回的是 `left`？」最后写了一份自己的总结让我检查。
- **卡点**：以为二分在「找 target」；以为 `right = mid - 1` 会把答案扔掉。
- **讲解过程**：
  1. **合并分支**：`>` 和 `==` 做的事一样 → 算法眼里只有 `< target` 和 `≥ target` 两种数。左边界 = **第一个 `≥ target` 的位置** = 两种数的分界线。
  2. **涂色 / 不变量**：`nums[mid] < target` → `mid` 及左边涂 🔵，`left = mid + 1`；`nums[mid] >= target` → `mid` 及右边涂 🔴，`right = mid - 1`。始终成立：**`left` 左边全是 `< target`，`right` 右边全是 `≥ target`**。
  3. **为什么返回 `left`**：结束时 `left = right + 1`，两指针相邻：`right` = 最后一个 `<`，`left` = 第一个 `≥` = 左边界（返回 `right + 1` 也一样）。
  4. **第一次 `mid` 就是答案**：`right = mid - 1` 不是扔掉 `mid`，而是把它涂红放到 `right` 右边。剩下的未知区间全是 `< target`，`left` 一步步推过去，正好停在它上面。`[1,2,3,4,5]` 找 3：`mid=2` → `right=1` → `left=1` → `left=2` 返回 2。多走的几步是「确认左边没有更早的 3」，复杂度仍是 O(log n)。
  5. **怎么想出来的**：把「找等于 target」换成「找满足条件的第一个位置」；定义 `left` / `right` 守护什么；结束时从定义读出答案（和 Q18 一样：先定义状态，代码从定义推出来）。
  6. **左右边界对照**：
     | 要找 | 两种颜色 | `==` 归哪边 | 答案 |
     |---|---|---|---|
     | 左边界（第一个 `≥`） | `<` / `≥` | `right = mid - 1` | `left` |
     | 右边界（最后一个 `≤`） | `≤` / `>` | `left = mid + 1` | `right` |
  7. **越界**：循环里 `0 <= left <= mid <= right <= n-1`，不会越界。循环结束后：`left` 可能 = `n`（target 比所有数大、空数组）→ `nums[left]` 报 `IndexError`；`right` 可能 = `-1`（target 比所有数小）→ ⚠️ `nums[-1]` **不报错，悄悄读最后一个元素**（Python 特有的坑）。
  8. **普通查找**：没找到时 `left`、`right` 同样会出界（用户自己指出的），只是直接 `return -1` 不去读它们。→ **指针出界本身不是错误，拿出界的指针读数组才是错误。** 而且那个 `left` 正好是**插入位置**（`bisect.bisect_left`、LeetCode 35）。
  9. **初始值和循环条件要配套**：闭区间 `right = n-1` + `<=` + `right = mid-1`；左闭右开 `right = n` + `<` + `right = mid`。`right = n` 配 `<=` → `mid` 可能 = `n` → 越界。
  10. `mid = left + (right - left) // 2` 是 Java/C++ 防整数溢出的习惯；Python 写 `(left + right) // 2` 也行。
  11. **用户的总结（检查后修正）**：
      1. 空数组可以提前 `return -1`；也可以不写，下面的检查会自动拦下（代入法）。
      2. 循环结束 `left = right + 1`；`right` 右边全 `≥ target`，`left` 左边全 `< target` → `left` 是左边界；`==` 归 `≥` 那边由 `right` 管，所以 `==` 时移动 `right`。右边界同理。
      3. 返回前查两件事：**① 没越界**（`left` 只往右走，只查上界；`right` 只往左走，只查下界）；**② 指着的值确实是 target**（target 可能不存在）。先①后②，利用短路：
         ```python
         if left >= len(nums) or nums[left] != target:
             return -1
         return left
         ```
         （用户原来只写了 `if left > len(nums)-1`，漏了②，见错题本 #28）
      4. 普通查找没找到时 `left` 也会出界，只是不用；它正好是插入位置。
- **结论**：二分不是找「等于」，而是找「`不满足 | 满足`」的分界线；`left` / `right` 各守一边，结束时相邻，答案从不变量直接读出来。用结束后的指针读数组前，先查越界、再查值。
- **待办**：① `[2,2,2]` 找 2 的右边界，结束时 `left`、`right` 各是多少？② 闭区间初始值配 `while left < right`，在 `[5]` 里找 5 会怎样？③ 普通查找把 `return -1` 改成 `return left`，`[1,3,5]` 找 3 返回什么？
- **关联**：Q9（指针的含义要一致）、Q18（先定义状态）、Q16（`and`/`or` 短路）；→ 错题本 #28

#### Q29 · 二分查找：`nums[mid] > target` 时为什么是 `right = mid - 1` 而不是 `right = mid`？
- **时间**：2026-11-08 17:36
- **原始问题**：「二分查找的时候如果 mid 的数值大于 target，为什么不能让 `right = mid`，而是 `mid - 1`？」
- **讲解过程**：
  1. **闭区间** `[left, right]` + `while left <= right`：`right` 本身是候选。`nums[mid] > target` → `mid` 肯定不是答案；`right = mid` 等于把已排除的 `mid` 放回候选。
  2. **死循环**：`nums = [5]`、`target = 3`：`left = right = mid = 0`，`right = mid` 什么都没变，`while` 永远成立。
     > 二分能结束，靠的是每一轮区间至少缩小一格；`mid ± 1` 保证这一点。
  3. **`right = mid` 什么时候对**：左闭右开 `[left, right)`，`right` 本身不是候选，`right = mid` 就表示「`mid` 及右边排除」；`left < right` 时 `mid < right`，每次都会缩小。
     | | 闭区间 | 左闭右开 |
     |---|---|---|
     | `right` 是候选吗 | 是 | 不是 |
     | 排除 `mid` 后 | `right = mid - 1` | `right = mid` |
     | 循环条件 | `left <= right` | `left < right` |
- **结论**：不是 `right = mid` 一定错，而是它和闭区间的定义不配套；选一套区间定义，所有地方跟着它写。
- **待办**：检验题：闭区间里 `nums[mid] < target` 写成 `left = mid`，`[1, 3]` 找 3 会怎样？（`left = 0, right = 1, mid = 0` → `left = 0` 不变 → 死循环）
- **关联**：Q26（二分边界）、Q9（指针含义要一致）

#### Q30 · LeetCode 1011 在 D 天内送达包裹：二分答案 + 计算天数的 `f` 写错了
- **时间**：2026-11-08 17:36
- **原始问题**：截图显示超出时间限制（Example 1）。代码：二分 `capacity`，`left, right = 1, 500`（求 `max` 和总和的两行被注释掉了），`f(weights, capacity)` 计算天数：
  ```python
  while i < len(weights):
      x = capacity
      while x - weights[i] >= 0 and i < len(weights) - 1:
          x -= weights[i]
          i += 1
      days += 1
      i += 1
  ```
  修改后又问「我改成这样」，然后写了总结「应该注意在此函数中执行 先查找，再更新 的原则」，请我写得更详细。
- **卡点**：装不下的货被跳过；最后一件货特殊处理；二分上下界错误。
- **讲解过程**：
  1. 本地跑贴出来的代码**没有超时**，返回 7（应为 15）；超时可能来自之前的版本。`f` 的天数偏少：`capacity = 10` → 4，`15` → 3。
  2. **Bug 1（漏货）**：`capacity = 10` 第一天装 1、2、3、4 后 `x = 0`，重 5 的那件装不下，内层停下；外层**无条件** `i += 1` → 5 被跳过，永远没上船。`i < len(weights) - 1` 让最后一件货永远靠外层 `i += 1`「假装装上」。
  3. **Bug 2**：`left = 1` → 容量可能比最重的货还小，那件货永远装不上，旧 `f` 却假装运走了。`left` 至少是 `max(weights)`。
  4. **Bug 3**：`right = 500` 不够，一天运完要总重量（最多 500 × 5×10⁴）。注释掉的 `for w in weights: left = max(left, w); right += w` 是对的。
  5. **修改后的版本**（随机对拍 3000 组全对）：
     ```python
     while i < len(weights):
         x = capacity
         while i < len(weights):
             if weights[i] <= x:      # 先检查
                 x -= weights[i]      # 再更新
                 i += 1
             else:
                 break                # 装不下：i 不动，留给明天
         days += 1
     ```
     小整理：`right` 从 0 累加（`1, 500` 里的 500 已经没意义）；`f` 在 `if` 和 `elif` 各调用一次 → 改 `else`；`x - w >= 0` 写成 `w <= x` 更直接。
  6. **另一种写法**：一件一件看货，`load + w > capacity` 就 `days += 1; load = 0`，再 `load += w`（初始值用代入法想：第一件货来之前）。
  7. **用户总结的详细版**：
     - **原则：先检查，再更新**——指针移动必须是「确认这一步成功了」的结果。`i` 的含义是「下一件待装的货」→ `i += 1` 只能出现在「这件货确实装上了」之后。
     - 旧写法错在：外层末尾无条件 `i += 1`，默认「内层停下时那件货已经处理了」，但内层是因为装不下才停的。最后一件货单独处理 → 两套逻辑更易错。（不是「溢出」，而是「还没装上，指针就走了」。）
     - **自查**：看到 `i += 1` 时问「`i` 原来指的那个元素，真的已经处理完了吗？」
     - **同类坑**：错题本 #12（3Sum 指针移动写在分支外）、#25（4Sum 先跳重复再处理）、#31（这次）——指针移动写在了无条件执行的位置。
     - **副作用**：先检查再更新之后，如果某件货永远装不下，`i` 永远不动 → 死循环 → 必须配合 `left = max(weights)`。
- **结论**：二分答案的框架是对的，关键在 `f`：指针只在操作成功后移动；二分的上下界要从题意推（最重的货 ~ 总重量）。
- **待办**：① 用自己的话回答：`capacity` 小于最重的货时，新 `f` 的外层每轮 `i`、`days` 怎么变？② 整理后提交。
- **关联**：Q26（二分）、Q18（代入法）、错题本 #12、#25；→ 错题本 #31、#32

#### Q32 · LeetCode 239 滑动窗口最大值：单调队列的 `pop` 看错了一头
- **时间**：2026-11-08 17:36
- **原始问题**：截图，两个示例通过但提交「解答错误」。
  ```python
  def pop(self, number):
      if self.max_queue[-1] == number:
          self.max_queue.popleft()
  ```
  追问：「是不是因为我还没有 pop 上一轮它就已经 push 进去了？」「没懂，不都是队尾吗？」
- **卡点**：以为 `[-1]` 和 `popleft()` 是同一头；怀疑 push / pop 的顺序有问题。
- **讲解过程**：
  1. 单调队列的 `push`（弹出队尾比新数小的）、`max()`（`q[0]`）和窗口逻辑都对。
  2. 随机对拍找到反例：`nums = [0, 5, 3, 2, 5], k = 2` → 你的 `[5, 5, 5, 5]`，期望 `[5, 5, 3, 5]`。
  3. **顺序没问题**：每轮 ① `push` 新数（k 个）→ ② 记录 `max` → ③ `pop` 最老的（剩 k-1 个，下一轮补满）。
  4. **两头**：
     ```
      队头（左）              队尾（右）
       [  5  ,  3  ,  2  ]
         [0]          [-1]
     ```
     `append` / `pop()` / `q[-1]` → 右边；`appendleft` / `popleft()` / `q[0]` → **左边**（带 left 的就是左）。
  5. `push` 从右边进 → **左边是最老的**，滑出窗口的是最老的 → 应该看左边 `q[0]`、删左边 `popleft()`。代入 `[5, 3]` 要删 5：`q[-1] = 3 ≠ 5` → 不删，5 赖着不走，下一窗口 `[3, 2]` 的 `max` 还是 5。
  6. 修成 `if self.max_queue[0] == number:` 后随机对拍 5000 组全对。
  7. 小整理：`if i < k-1` 和 `else` 两个分支第一行都是 `push`，提到外面（代入法：并排找相同部分）。
- **结论**：「检查」和「删除」必须是同一头；deque 里 `[0]` / `popleft` 是左边，`[-1]` / `pop` 是右边。
- **待办**：用户还没回答「`q[?]` 应该填几」（应为 `q[0]`）；改好后提交。
- **关联**：Q17（单调栈）、Q31（deque 两头）；→ 错题本 #33

#### Q37 · LeetCode 141 环形链表：`while fast.next is not None` 报 `AttributeError`
- **时间**：2026-11-08 19:46（追问 19:50）
- **原始问题**：截图，`head = [1, 2]` 报 `AttributeError: 'NoneType' object has no attribute 'next'`，出错行 `while fast.next is not None:`。追问：「所以 fast 可能走到最后一个节点，也有可能变成 None？」
- **卡点**：只检查了 `fast.next`，没想到 `fast` 自己会变成 None。
- **讲解过程**：
  1. 跟踪 `[1, 2]`：开始 `fast = 1`，`fast.next = 2` ✅ 进入循环；`fast = fast.next.next = None`；回到 `while` 对 None 取 `.next` → 💥。报错里的 `'NoneType' object` 就是 None。
  2. fast 每次走两步，走到头时取决于长度奇偶：
     | 情况 | `fast` | `fast.next` | 能走两步吗 |
     |---|---|---|---|
     | 偶数长度 `[1,2]` | `None` | 取不了 💥 | ❌ |
     | 奇数长度 `[1,2,3]` | 最后一个节点 | `None` | ❌ |
     | 没走到头 | 节点 | 节点 | ✅ |
     有环的话 fast 永远走不到 None。
  3. 修正：`while fast and fast.next:`。**顺序不能反**：`and` 短路，`fast` 是 None 时后面的 `fast.next` 不会执行。
  4. 规律：**要访问 `x.next.next`，就要先保证 `x` 和 `x.next` 都不是 None——访问几层，检查几层**（和二分「先检查越界再读值」同一个思路）。
  5. 小问题：141 返回 True / False，签名却写 `-> Optional[ListNode]`（从 142 复制的），应为 `-> bool`。
- **结论**：快指针走两步，循环条件写 `while fast and fast.next`。
- **待办**：检验题未答：改完之后开头的 `if head is None: return False` 还需要吗？（不需要：`fast = None` 时 while 直接不进，返回 False）
- **关联**：Q36、Q26（短路）、Q17（`while s and ...`）；→ 错题本 #34

#### Q38 · LeetCode 21 合并两个有序链表：不用虚拟头节点应该怎么写？
- **时间**：2026-11-09 13:14
- **原始问题**：贴出用 `dummy = ListNode(-1)` 的标准写法：「这个使用了虚拟头节点法，如果不使用的话应该怎么写呢？」
- **讲解过程**：
  1. 不用 dummy 就要**单独处理第一个节点**：一开始还没有 `p` 可以接。
     ```python
     def mergeTwoLists(self, list1, list2):
         if list1 is None:              # 特殊情况 1：有一条是空的
             return list2
         if list2 is None:
             return list1
         if list1.val <= list2.val:     # 特殊情况 2：先选出头节点
             head = list1
             p1, p2 = list1.next, list2
         else:
             head = list2
             p1, p2 = list1, list2.next
         p = head
         while p1 is not None and p2 is not None:   # 后面和 dummy 版完全一样
             if p1.val <= p2.val:
                 p.next = p1; p1 = p1.next
             else:
                 p.next = p2; p2 = p2.next
             p = p.next
         p.next = p1 if p1 is not None else p2
         return head
     ```
  2. 「选头节点」那段其实是把循环体手动执行了一次，容易出错（比如忘了 `list1.next`，同一个节点被接两次）。
  3. **dummy 就是代入法里的哨兵**：第一轮特殊，是因为还没有「前一个节点」可写 `p.next`；dummy 提供一个假的前一个节点，让第一个真节点也走通用代码。
     | | 特殊情况 | 哨兵 |
     |---|---|---|
     | 前缀和 | 第 0 个前面没东西 | `preSum[0] = 0` |
     | 单调栈 | 栈是空的 | `s and ...` |
     | 求最大值 | 还没有 best | `best = -inf` |
     | 链表 | 头节点前面没节点 | `dummy` |
  4. 小写法：`p.next = p1 or p2`（`p1` 是 None 时返回 `p2`）。
- **结论**：虚拟头节点 = 链表版的哨兵，用一个假的前驱把「第一个节点」的特殊情况消掉，最后返回 `dummy.next`。
- **待办**：检验题未答：dummy 版里两条链表都为空时返回什么？（while 不执行，`p.next = None`，返回 `dummy.next = None`，正确）
- **关联**：Q18（代入法）

#### Q39 · LeetCode 23 合并 K 个升序链表：堆里放的是什么？按哪个值排？`__lt__` 重载什么、哪里用到？+ 我的代码两个 bug
- **时间**：2026-11-09 13:59（代码审查 14:28）
- **原始问题**：看参考代码 `heapq.heappush(pq, (head.val, i, head))`：「这里的 heappush 为什么 push 进去那么多元素？它怎么知道按照哪个值进行排列大小？这个重载运算符是重载什么，哪里用到了？」之后贴出自己写的版本 + 报错截图 `AttributeError: 'NoneType' object has no attribute 'val'`。
- **卡点**：以为一次 push 了三个元素；不清楚元组如何比较；不知道 `__lt__` 的作用。
- **讲解过程**：
  1. **每次只 push 一个元素**：`heappush` 只有两个参数，`pq` 和**一个元组** `(val, i, node)`。取出时解包：`val, i, node = heapq.heappop(pq)`。
     | 位置 | 内容 | 作用 |
     |---|---|---|
     | `[0]` | `val` | 排序用 |
     | `[1]` | `i`（第几条链表） | 平局时决胜 |
     | `[2]` | `node` | 弹出后接到结果上 |
  2. **按哪个值排**：`heapq` 是最小堆，用 `<` 比较；**元组的 `<` 从左往右逐个比**（像查字典）→ val 放第一位，就主要按 val 排。
  3. **`i` 的作用**：val 相等时元组会去比第二个。没有 `i` 就会比到 `node`，自定义类默认不能比较 → `TypeError: '<' not supported between instances of 'ListNode' and 'ListNode'`。堆里同一时刻每条链表最多一个节点，`i` 一定不同，永远比不到 node。
  4. **`__lt__` = less than，重载的是 `<`**：`a < b` → `a.__lt__(b)`（bound method，Q1）。同类：`==` → `__eq__`，`print(a)` → `__str__`，`len(a)` → `__len__`。
  5. **这段代码里 `__lt__` 其实没用到**：有 `i` 兜底，比不到节点。它在「直接把节点放进堆」时才有用：`heappush(pq, head)`。两种写法选一种。LeetCode 的 ListNode 是系统定义的，加不了 `__lt__`，所以一般用元组 + `i`。
  6. **我的代码两个 bug**：
     - `lists = [[]]`：`lists` 本身不空（`if not lists` 拦不住），里面的链表是空的 → `head` 是 None → `head.val` 💥。push 前要加 `if head is not None:`。外面的容器空不空，和里面的元素空不空，是两回事。
     - `val, i, head = heappop(pq)` 漏了 `heapq.` → `NameError`。要么写 `heapq.heappop`，要么 `from heapq import heappop, heappush`。
- **结论**：堆里放 `(val, i, node)` 一个元组；元组从左往右比较，val 决定顺序，`i` 防止比到节点；`__lt__` 定义 `<`，只有直接放节点时才用得到。
- **待办**：检验题未答：去掉 `i` 也不写 `__lt__`，`lists = [[1, 4], [1, 3]]` 会怎样？（两个 val 都是 1 → 比较节点 → TypeError）
- **关联**：Q1、Q14（解包）、Q27（`__str__`）、Q36、Q40；→ 错题本 #35

#### Q41 · LeetCode 160 相交链表：两种「走到头换到另一条」的写法有什么区别？不相交时第二种会一直空转吗？
- **时间**：2026-11-09 15:32
- **原始问题**：截图，对比两种写法：
  ```python
  # 上（注释掉的）
  p1 = p1.next if p1.next is not None else headB
  # 下（通过的）
  p1 = headB if p1 is None else p1.next
  ```
  「这上下有什么区别？第二种遇到非交叉的难道不会一直空转吗？」
- **卡点**：直觉反了——会空转的是上面那种。
- **讲解过程**：
  1. 区别只有一处：**指针会不会停在 None 上**。上面看 `p1.next`，p1 永远不会变成 None；下面看 `p1`，会先走到 None，下一步才跳到另一条。
  2. 不相交例子 A = `1 → 2`，B = `3`，下面的写法：
     | 步 | p1 | p2 |
     |---|---|---|
     | 0 | 1 | 3 |
     | 1 | 2 | None |
     | 2 | None | 1 |
     | 3 | 3 | 2 |
     | 4 | **None** | **None** ← 相等，退出 |
     两人路程相同：A 的 2 个 + 1 个 None + B 的 1 个 = B 的 1 个 + 1 个 None + A 的 2 个 = 4 步，所以会**同时**走到最后那个 None。**None 就是不相交时的「虚拟交点」**。
  3. 上面的写法：p1 = `1, 2, 3, 1, 2, 3, ...`，p2 = `3, 1, 2, 3, 1, 2, ...`，跳过了 None，在节点间一直转，永远不相等 → **死循环**。另外 `headA` 一开始是 None 时，`p1.next` 直接 `AttributeError`。
- **结论**：「让指针真的走到 None」这一步不能省：它让两人路程相等，不相交时在 None 处相遇。
- **待办**：检验题未答：两条链表**相交**时，上面那种跳过 None 的写法能找到 c1 吗？（能：p1 路程 a + c + b，p2 路程 b + c + a，相等，会在 c1 相遇；只是不相交时死循环）
- **关联**：Q37（访问 `.next` 前先确认不是 None）；→ 错题本 #37

#### Q42 · LeetCode 206 反转链表（递归）：`if head is None: return None` 是不是专门为 `[]` 写的？
- **时间**：2026-11-09 21:18
- **原始问题**：
  ```python
  def reverseList(self, head):
      if head is None:
          return None
      if head.next is None:
          return head
      last = self.reverseList(head.next)
      head.next.next = head
      head.next = None
      return last
  ```
  「`if head is None: return None` 这个语句是不是特意为了 `[]` 这样的 case？如果是正常的测试用例，也会正常运行的吧？」
- **讲解过程**：
  1. 猜对了：**只有 `[]` 会用到**。递归传的是 `head.next`，能走到递归那一行说明 `head.next` 不是 None → 每次递归传进去的都是真实节点，最后停在最后一个节点（命中第二个判断）。
     | 输入 | 命中哪个判断 |
     |---|---|
     | `[]` | 第一个，且只在最开始那次调用 |
     | `[1,2,3,4,5]` | 每层都不命中第一个；最深一层（节点 5）命中第二个 |
  2. **不能删**：删了以后 `[]` 会执行 `None.next` → `AttributeError`。
  3. 可以合并：`if head is None or head.next is None: return head`（head 是 None 时返回的就是 None）。靠 `or` 短路：前半句成立时 `head.next` 不会执行。
- **结论**：第一个判断只防空输入，但必须有；合并写法要把 `head is None` 放在前面。
- **待办**：检验题未答：反过来写 `if head.next is None or head is None:`，输入 `[]` 会怎样？（先执行 `None.next` → AttributeError）
- **关联**：Q37、Q40、Q26（短路）

#### Q43 · 高度平衡二叉树的高度是 O(log N)：4 个节点的树高度是 3，公式算出来是 2，为什么？
- **时间**：2026-11-10 18:32
- **原始问题**：看到「N 个节点的高度平衡二叉树高度是 O(log N)」：「如果我只取 1、2、3、4 这四个节点的高度平衡树，可以看出来这个高度是 3，但是根据公式算出来高度是 2，为什么？」
- **卡点**：把 O(log N) 当成了能精确算出高度的等式。
- **讲解过程**：
  1. **O(·) 藏了常数**：O(log N) 的意思是「存在常数 c，使高度 ≤ c · log N」，只说增长速度同级，不管 c 是几、也不管 ±1（和 dict 查找 O(1) 不是「正好 1 步」一样）。
  2. **高度有两种数法**：1-2-4 这条路径按节点数是 3、按边数是 2，差的 1 O(·) 不管。按边数「算对」只是巧合。
  3. 真实上界（按节点数）：满二叉树正好 log₂(N+1)；高度平衡树最坏约 1.44 · log₂N。
  4. **1、2、3、4 正好是最坏情况**：高度 h 的平衡树最少节点数 1, 2, 4, 7, …，满足 `最少(h) = 最少(h-1) + 最少(h-2) + 1`（类斐波那契，每层约 ×1.618 → 1/log₂1.618 ≈ 1.44）。
  5. 为什么重要：退化成链表时高度是 N；N = 100 万时，链表高度 100 万，平衡树最多约 29。差的是数量级。
- **结论**：O(log N) 描述的是增长速度，不是可以代数计算的准确高度；平衡树最坏高度约 1.44 log₂N。
- **待办**：检验题未答：满二叉树高度 4（按节点数）有几个节点？（15，log₂16 = 4）
- **关联**：Q8（复杂度）、Q34（「平均 O(1)」）、Q52（BST 操作的 O(log N)）；→ 错题本 #38

#### Q47 · LeetCode 102 层序遍历：输出少了最后一层；`cur = dq[0]` 不会「动态锁定」队头吗？
- **时间**：2026-11-10 20:26（追问 20:27）
- **原始问题**：截图，输出 `[[3],[9,20]]`，期望 `[[3],[9,20],[15,7]]`：
  ```python
  while dq:
      sz = len(dq)
      cur = dq[0]                      # 写在 for 外面
      for _ in range(sz):
          if cur.left is not None:
              dq.append(dq[0].left)
          if cur.right is not None:
              dq.append(dq[0].right)
          tmp.append(dq.popleft().val)
      res.append(tmp)
      tmp = []
  ```
  追问：「cur 不是动态锁定这个队列的头？」
- **卡点**：以为 `cur = dq[0]` 会跟着队头自动变。
- **讲解过程**：
  1. 第 2 层：`dq = [9, 20]`，`cur = 9`。for 第 1 次：9 没孩子，pop 9；第 2 次：`cur` **还是 9** → 不加孩子 → pop 20。20 的孩子 15、7 从没被检查。
  2. **赋值绑定的是对象，不是表达式**：`cur = dq[0]` = 执行那一刻把 `cur` 这张标签贴到当时的队头节点上，之后队列怎么变都不影响，除非**再赋一次值**。
     ```python
     lst = ["a", "b", "c"]
     x = lst[0]
     lst.pop(0)
     print(x)        # "a"，不会变成 "b"
     ```
  3. 修正：在 for 里每次重新取，并统一用 `cur`：`cur = dq.popleft()`，然后用 `cur.left` / `cur.right` / `cur.val`，`dq[0]` 在循环里完全不出现。`depth = 1` 没用到，可删。
- **结论**：变量是贴在对象上的标签，不会「追踪」表达式；要每轮都是当前队头，就在循环里每轮重新赋值。
- **待办**：用户还没贴出改好的代码
- **关联**：Q1（名字标签）、Q31（deque）、错题本 #1–#3；→ 错题本 #41

#### Q48 · LeetCode 111 二叉树的最小深度：用 `self.depth` 计数，为什么结果偏大？
- **时间**：2026-11-11 11:47
- **原始问题**：「为什么不正确呢？」用例 `[3,4,5,-7,-6,null,null,-7,null,-5,null,null,null,-4]`，期望 2，提交输出 3。
  ```python
  def minDepth(self, root):
      if root is None:
          return 0
      self.depth += 1
      if root.left is None and root.right is None:
          self.minimum_depth = min(self.depth, self.minimum_depth)
          return self.minimum_depth            # 出口 1：没减
      if self.depth > self.minimum_depth:
          return self.minimum_depth            # 出口 2：没减
      self.minDepth(root.left)
      self.minDepth(root.right)
      self.depth -= 1
      return self.minimum_depth                # 出口 3：减了
  ```
- **卡点**：不知道 depth 在哪里「漂」了。
- **讲解过程**：
  1. 本地加打印跑这个用例：
     ```
     enter 3   depth 1
     enter 4   depth 2
     enter -7  depth 3
     enter -7  depth 4
     enter -6  depth 4   ← 应该是 3
     enter -5  depth 5   ← 应该是 4
     enter 5   depth 4   ← 应该是 2！
     ```
     本地输出 4（提交的版本输出 3，可能略有不同），都不对，原因相同：**depth 只涨不降**。
  2. depth 像楼层计数器：进入 +1，离开 −1，**每次进入都必须对应一次离开**。这个函数 `+= 1` 之后有三个出口，只有最后一个减了 → 叶子节点（-7）和剪枝（-5）走的出口都漏了 `-= 1`。
  3. 引导用户自己数出口、自己改（每个出口返回前都要减回来）。更根本的写法：**把 depth 当参数传下去**，参数在函数返回时自然消失，不用手动撤销（见 Q53）。
- **结论**：用共享变量记录「当前深度」时，函数的**每一个出口**都要撤销进入时的修改；漏一个就会越算越大。
- **待办**：用户还没改；可以对比参数传递写法 `traverse(node, depth)`
- **关联**：Q46（共享状态）、Q51（回溯：做选择 / 撤销选择）、Q53（参数传递）；→ 错题本 #42

#### Q49 · 快速排序：两个 `sort` 有什么区别？`@staticmethod` 是什么？`partition` 怎么实现？i、j 交换后要回到起点吗？
- **时间**：2026-11-11 12:15（追问 12:23）
- **原始问题**：贴出 `Quick` 类（`sort` / `sort_` / `partition`，都是 `@staticmethod`）：「两个 sort 有什么区别？static method 是什么意思？这里的 partition 是怎么实现的？」追问：「每次交换 i 和 j 需要重新返回到初始位置吗？先 i 然后 j？第三轮我觉得如果 i 先动的话，应该 i 停在 9 那里，j 也在 9 那里。」
- **卡点**：以为 j 也会停在 9（把 i、j 的停止条件搞成了一样）。
- **讲解过程**：
  1. **两个 sort**：`sort(nums)` 是对外入口，只做一次性的事（`random.shuffle` 防最坏情况、调用 `sort_(nums, 0, len-1)`）；`sort_(nums, lo, hi)` 是递归干活的函数，需要区间参数。打乱写进递归会每层打乱一次，又慢又会弄乱排好的部分。末尾的 `_` = 「内部用」。
  2. **`@staticmethod`**：写在类里但**没有 self** 的函数，用 `Quick.sort(nums)` 调用，不用创建对象。快排不存状态，类只起分组作用。内部调用要写 `Quick.sort_(...)`（LEGB 跳过 class，见 Q46）。
  3. **partition**：`pivot = nums[lo]`，目标是整理成 `[≤pivot | pivot | >pivot]`，返回 pivot 的下标。
     - `i` 从左往右，**跳过 ≤pivot**，停在第一个 **>pivot**
     - `j` 从右往左，**跳过 >pivot**，停在第一个 **≤pivot**
     - 都停下且 `i < j` → 交换这两个放错位置的元素，继续；`i >= j` → 结束
     - 最后 `nums[lo]` 和 `nums[j]` 交换，返回 `j`
     例 `[4, 7, 2, 9, 1, 4]`，pivot = 4：
     | 轮 | i 停在 | j 停在 | 操作 | 数组 |
     |---|---|---|---|---|
     | 1 | 1（7） | 5（4） | 交换 | [4, 4, 2, 9, 1, 7] |
     | 2 | 3（9） | 4（1） | 交换 | [4, 4, 2, 1, 9, 7] |
     | 3 | 4（9） | 3（1） | i ≥ j，break | 不变 |
     | 收尾 | | | lo ↔ j | [1, 4, 2, 4, 9, 7]，返回 3 |
     `i < hi`、`j > lo` 是防越界（先判边界再访问）。
  4. **追问**：交换后**不回起点**，从当前位置继续 → i 只往右、j 只往左，合起来扫一遍，O(n)。每轮先 i 后 j。第三轮 j 不会停在 9：9 > pivot 对 i 是停止信号，对 j 是**要跳过的**。结束时两指针交错、相邻：`j = i - 1`，j 指向 ≤pivot 区域的最后一个 → pivot 应该去的位置。交换后不写 `i += 1, j -= 1`，下一轮会重新检查刚换的两个，立刻跳过。
- **结论**：i 停在 >pivot、j 停在 ≤pivot，交换放错的一对，不回头；交错后 j 就是 pivot 的最终位置。
- **待办**：检验题未答：① 为什么最后和 `nums[j]` 而不是 `nums[i]` 交换？（结束时 `nums[j]` ≤ pivot、`nums[i]` > pivot；把 >pivot 的换到最左边会破坏左半边）② 手动 partition `[5, 1, 8, 3]`（第 1 轮 i=2、j=3 交换 → `[5,1,3,8]`；第 2 轮 i=3、j=2 break；收尾 → `[3,1,5,8]`，返回 2）
- **关联**：Q44（staticmethod vs 方法 vs 嵌套函数）、Q46（LEGB）、Q11（双指针）；→ 错题本 #44

#### Q50 · LeetCode 543 二叉树的直径：思路对，代码哪里错？
- **时间**：2026-11-11 13:44
- **原始问题**：（只贴代码）注释写着「diameter 其实就是某一个点的左子树深度 + 右子树深度，令 diameter 最大；如何知道左右子树深度？后序遍历」。
  ```python
  def __init__(self):
      self.max_diameter = float("-inf")
  def diameterOfBinaryTree(self, root):
      self.traverse(root)
      return self.max_diameter
  def traverse(self, root: Optional(TreeNode)):
      if root is None:
          return 0
      left = self.diameterOfBinaryTree(root.left)     # 调错了函数
      right = self.diameterOfBinaryTree(root.right)
      self.max_diameter = max(left + right, self.max_diameter)
      return max(left, right) + 1
  ```
- **卡点**：入口函数和辅助函数的返回值混了。
- **讲解过程**：
  1. 思路完全正确（标准解法）。本地跑 `[1,2,3,4,5]`（应为 3）和空树，都输出 `-inf`。
  2. **主要 bug**：递归应该调 `self.traverse`（返回**深度**），却调了 `self.diameterOfBinaryTree`（返回 **max_diameter**）。叶子节点调 `diameterOfBinaryTree(None)` → 里面 `traverse(None)` 返回的 0 被丢掉，返回的是 `-inf` → 全部变成 `-inf`。
  3. 初始值 `-inf`：空树时从没被更新，返回 `-inf`；直径最小是 0，应初始化为 0。
  4. `Optional(TreeNode)` → `Optional[TreeNode]`（Python 3.13 直接 `TypeError`）。
- **结论**：拆成「入口 + 递归辅助」时，递归一定调辅助函数；初始值按题意的最小可能值设。
- **待办**：用户还没改；改后叶子节点的 `left`、`right` 应为 0
- **关联**：Q44、Q49（入口函数 vs 递归函数）；→ 错题本 #43

#### Q51 · 回溯算法框架（全排列）是什么意思？
- **时间**：2026-11-11 14:54
- **原始问题**：贴出 Java 回溯核心代码（for 循环里 `used[i] = true; track.addLast(nums[i]); backtrack(nums); track.removeLast(); used[i] = false;`）：「这是什么意思？」
- **讲解过程**：
  1. 例子：全排列 `[1, 2, 3]`，相当于把 3 个数依次放进 3 个空位，画成一棵「选择树」：
     ```
                       []
             /         |         \
           [1]        [2]        [3]
          /   \      /   \      /   \
      [1,2] [1,3] [2,1] [2,3] [3,1] [3,2]
        |     |
     [1,2,3] [1,3,2] …
     ```
     `backtrack` 就是把这棵树完整走一遍：`track` = 当前路径，`used[i]` = 第 i 个数用过没，`for` = 这一层挨个尝试。
  2. 每次循环三步：**做选择**（标记 + 加入路径）→ **进入下一层** → **撤销选择**（拿掉 + 取消标记）。撤销是为了让路径恢复原样，才能去试别的分支 → 「回溯」= 走下去再退回来。
  3. 和 Q48 同一个道理：**做了什么就要撤销什么，成对出现**。
  4. 这段代码不完整，还缺：
     ```java
     if (track.size() == nums.length) {          // ① 结束条件：走到叶子，记录
         res.add(new LinkedList<>(track));
         return;
     }
     for (int i = 0; i < nums.length; i++) {
         if (used[i]) continue;                   // ② 跳过用过的数
         ...
     }
     ```
- **结论**：回溯 = 遍历选择树；框架是「结束条件 + for 里 做选择 → 递归 → 撤销选择」。
- **待办**：检验题未答：为什么要 `res.add(new LinkedList<>(track))` 复制一份，而不是 `res.add(track)`？（track 后面会被不断 `removeLast`，存的是同一个对象 → 最后 res 里全是同一个空列表）
- **关联**：Q48（进入 / 离开要对称）、错题本 #1–#3（名字标签与引用）

#### Q52 · BST 节点维护 `size` 字段：怎么推导出某个节点的排名（找第 k 小）？rank 为什么是 1 而不是 4？
- **时间**：2026-11-11 15:54（追问 16:01）
- **原始问题**：看 230 题解里「每个节点记录以自己为根的子树有多少节点」：「怎么通过 size 来推导出 node 的排名？」追问（引用「在节点 4：左子树为空，rank = 1」）：「rank 怎么是 1？不是 4 嘛？」
- **卡点**：把局部排名和全局排名混了。
- **讲解过程**：
  1. 核心：BST 里左子树全比 node 小 → **node 在以自己为根的子树里排第 `left.size + 1` 名**（左子树空时 size 当 0）。
  2. 找第 k 小，比较 `k` 和 `rank = left_size + 1`：
     | 情况 | 怎么走 |
     |---|---|
     | `k == rank` | 返回 node |
     | `k < rank` | 去左子树，k 不变 |
     | `k > rank` | 去右子树，`k -= rank`（左子树 + node 自己已占 rank 个名次） |
     ```python
     def kthSmallest(root, k):
         node = root
         while node:
             left_size = node.left.size if node.left else 0
             rank = left_size + 1
             if k == rank:
                 return node.val
             elif k < rank:
                 node = node.left
             else:
                 k -= rank
                 node = node.right
     ```
     例：树 5(3(2(1), 4), 6)，找 k = 4：节点 5 rank 5 → 左；节点 3 rank 3 → 右，k = 1；节点 4 rank 1 == k → 答案 4。
  3. 每步只走一边 → O(树高)；平衡时 O(log N)（Q43）。代价：增删时路径上每个节点的 size 都要维护。
  4. **追问**：代码里的 rank 是**局部排名**（只算当前子树）。全局排名藏在 `k -= rank` 里：**全局排名 = 已扣掉的名次 + 局部 rank = 3 + 1 = 4**。往右走时比答案小的那些已经确定排在前面，扣掉以后到每个节点，k 和 rank 都是相对当前子树的，可以直接比较（类比：找全校第 4 名，A 班占了前 3 名 → 去 B 班找 B 班第 1 名）。
- **结论**：node 在自己子树里排第 `left.size + 1`；往右走时把左边已占的名次从 k 里扣掉，k 始终是「在当前子树里的第几名」。
- **待办**：检验题未答：同一棵树找 k = 6，每步节点、rank、k 是多少？（5：rank 5，k = 6 > 5 → 右，k = 1；6：rank 1 == 1 → 答案 6；扣掉 5 + 局部 1 = 6）
- **关联**：Q43、Q26（二分思想）、Q53

#### Q53 · LeetCode 98 验证 BST：只比较左右孩子为什么不对？传 `(min, max)` 为什么能和所有祖先比较？
- **时间**：2026-11-11 17:03（追问 17:04、17:05，用户总结 17:07）
- **原始问题**：题解里先给出「只比较自己和左右孩子」的错误写法，再给出带 `min`、`max` 参数的正确写法：「第二个解法我没看懂，有啥区别吗？」追问：「为什么能跟所有祖先比较？我认为只能跟他的直接父亲节点进行比较。」「max 会被更新吗？如果 4 有左子节点的话。」
- **卡点**：以为每个节点只能拿到父亲的信息，所以只能和父亲比。
- **讲解过程**：
  1. 区别：解法一每个节点只和**左右孩子的值**比（一层）；解法二和祖先传下来的**允许范围 (min, max)** 比。
  2. 反例：
     ```
             7
           /   \
          4     9
           \
            8      ← 在 7 的左子树里，却比 7 大
     ```
     解法一：每对父子都没问题 → 误判合法。8 必须 < 7 这条约束来自**爷爷**，4 只看孩子看不到。
  3. 解法二往下传时区间越收越窄：往左 → 上限换成当前节点；往右 → 下限换成当前节点；另一边照搬。
     | 节点 | 允许范围 | 检查 |
     |---|---|---|
     | 7 | (无, 无) | ✅ |
     | 4 | (无, 7) | ✅ |
     | 8 | (4, 7) | 8 ≥ 7 ❌ → False |
  4. **追问 1：只从父亲那里接收，怎么能和所有祖先比？** 父亲交出的不只是自己的值，而是**父亲手里的整个区间**，里面已经有祖先的约束（传话：爷爷对爸爸说「不许超过 7」，爸爸对孩子说「不许低于 4，而且爷爷说不许超过 7」）。祖先约束再多，只有最紧的上限和下限有用 → 永远压缩成两个数。
  5. **追问 2：max 会更新吗？** 会，往左走就更新。4 的左孩子 x 拿到 (无, 4)：同时受 < 4 和 < 7 约束，只留更紧的 4；新 max 一定比旧的小（当前节点本身就在旧区间里），直接替换即可。4 的右孩子 8 拿到的仍是 (4, 7)：`min`、`max` 是**参数**，每次递归调用各有一份，互不影响，也不需要手动撤销（对比 Q48 的 `self.depth`）。
  6. **用户总结（确认正确）**：「这样的方法可以框定一个范围，范围可以涵盖之前父节点的内容，而不像第一个解法只是比较一个值。」补充：区间只保留最紧的两条约束，每个节点比较两次，整体 O(N)。另一种思路：BST 的中序遍历严格递增。
- **结论**：一个节点是否合法取决于**所有祖先**；用参数把收紧后的 `(min, max)` 沿路径传下去，就能用两个数概括全部祖先约束。
- **待办**：检验题未答：① 9 的左孩子范围是多少？值为 6 时合法吗？（(7, 9)；6 ≤ 7 不合法）② x = 5（4 的左孩子）时解法二在哪发现？解法一能发现吗？（解法二：x 的范围 (无, 4)，5 ≥ 4 → False；解法一：节点 4 检查左孩子 5 ≥ 4 也能发现——这个反例两种都能抓到，因为违反的是父亲的约束）
- **关联**：Q48（参数传递 vs 共享变量）、Q52（BST 性质）

#### Q54 · 98 验证 BST（传 `(lo, hi)` 版）：算遍历还是分解问题？算前序吗？为什么 `return` 不在前序位置？
- **时间**：2026-11-11 17:41（追问 17:45、17:46、17:48、17:56、18:04）
- **原始问题**：贴出自己写的 98：
  ```python
  def isValidBST(self, root):
      return self.traverse(root, None, None)
  def traverse(self, root: Optional(TreeNode), min: Optional(TreeNode), max: Optional(TreeNode)):
      if root is None:
          return True
      if min is not None and root.val <= min.val:
          return False
      if max is not None and root.val >= max.val:
          return False
      left = self.traverse(root.left, min, root)
      right = self.traverse(root.right, root, max)
      return left and right
  ```
  「这个算遍历树求解还是分解问题？BST 合法意味着左右子树合法，但后序位置没有判断这个节点和左右子树的关系。」追问：「所以算前序遍历分解问题判断？」「比较别扭，如果是前序遍历，return 应该也写在前序位置」「完全后序遍历分解问题是不是更方便？后序得到的信息更全面」「那这个算前序遍历吗？」「我现在觉得这个算是遍历思想来求解」
- **卡点**：① 把「前序/后序」和「最后那个 `return` 写在哪」绑在一起；② 以为后序位置没有检查「节点和子树的关系」；③ 以为后序信息「更全面」。
- **讲解过程**：
  1. **「节点和子树的关系」在哪检查**：根的约束被放进参数传下去：`traverse(root.left, lo, root)` 表示「左子树每个节点都要 < root」。左子树的**每个节点**在自己的前序位置检查一次，而不是 root 在后序位置一次查完。
  2. **三个位置各做一件事**：
     | 位置 | 做什么 | 用到的信息 |
     |---|---|---|
     | 前序 | 检查自己是否违反 (lo, hi) | 从上面**传下来**的参数 |
     | 递归 | 把收紧后的范围传给子树 | — |
     | 后序 | `left and right` 组合答案 | 从下面**交上来**的返回值 |
  3. **「x 序」≠ `return` 的位置**：「x 序」说的是**当前节点自己的那件事**在递归之前 / 之间 / 之后做。只要答案要用子问题的结果，最后的 `return` 一定在递归之后。反例：前序遍历的分解写法 `return [root.val] + preorder(left) + preorder(right)`，结果是前序，`return` 却最后执行。中途的 `return False` 才是写在前序位置的，作用是**提前结束**。
  4. **验证是前序**：在检查前 `print(root.val)`，树 `2(1, 3)` 打印 2, 1, 3。
     | 版本 | 检查发生在 | 打印顺序 |
     |---|---|---|
     | 传 (lo, hi) | 递归之前 | 2, 1, 3 → 前序 |
     | 返回 (ok, min, max) | 递归之后 | 1, 3, 2 → 后序 |
     | 中序 + prev | 左右递归之间 | 1, 2, 3 → 中序 |
  5. **纯后序版**（信息往上交）：
     ```python
     def check(self, node):     # 返回 (是否合法, 子树最小值, 子树最大值)
         if node is None:
             return True, float('inf'), float('-inf')
         l_ok, l_min, l_max = self.check(node.left)
         r_ok, r_min, r_max = self.check(node.right)
         ok = l_ok and r_ok and l_max < node.val < r_min
         return ok, min(l_min, node.val), max(r_max, node.val)
     ```
     「后序信息更全面」要修正：前序知道**祖先**的约束，后序知道**子树**的情况，方向不同，不是谁更全面。这道题前序版更简单（2 个参数、空节点直接 True、违规能立刻停）；后序版要维护 min/max 和哨兵，默认算完整棵树。
     **必须用后序的情况**：问的是「每棵子树本身的性质」，如 1373 二叉搜索子树的最大键值和（要知道子树是否 BST、min、max、和）。
     > 约束来自上面 → 参数往下传，前序检查；要知道下面的情况 → 返回值往上交，后序计算。
  6. **用户最后的判断「本质是遍历」是对的**。更本质的判断方法：
     > 把返回值换成外部变量之后，算法还能**原样**工作吗？能 → 本质是遍历；不能（父节点必须拿子树结果做计算）→ 本质是分解问题。
     | 写法 | 父节点需要子树的什么 | 本质 |
     |---|---|---|
     | 前序传 (lo, hi) | 只要「有没有违规」，换成 `self.ok` 也行 | 遍历（形式上用了返回值） |
     | 中序 + prev | 什么都不需要 | 遍历 |
     | 后序 (ok, min, max) | 必须拿到左子树 max、右子树 min | 分解问题 |
  7. 代码小问题：`Optional(TreeNode)` 第 4 次圆括号；参数名 `min` / `max` 遮住内置函数，改成 `lo` / `hi`；可写 `return self.traverse(左...) and self.traverse(右...)` 利用短路。
- **结论**：前序 / 中序 / 后序看「当前节点的事在递归前、中、后做」，跟最后的 `return` 写在哪无关；遍历 vs 分解看「返回值能不能被外部变量原样替换」。传 (lo, hi) 版本质是遍历，后序 (ok, min, max) 版才是真正的分解。
- **待办**：
  - 检验题未答：104 最大深度两种写法分别是什么思想？（① `return max(左, 右) + 1` → 分解；② 带 depth 参数、叶子处更新 `self.res` → 遍历）
  - 检验题未答：遍历版里的 `or not self.ok` 有什么用？（发现违规后剪枝，不影响结果，只影响效率）
- **关联**：Q53（98 传 (min, max)）、Q55、Q56、Q57；→ 错题本 #46、#47

#### Q55 · 98 后序版能不能不返回 3 个值？`min(l_min, node.val)` 里 `l_min` 不是一定最小吗？
- **时间**：2026-11-11 17:49（追问 17:53）
- **原始问题**：「你可以不可以不用 return 3 个值？」看后序版的 `return ok, min(l_min, node.val), max(r_max, node.val)`：「最后为什么 return 要 `min(l_min, node.val)`，`l_min` 不是一定必须是最小的吗？」
- **卡点**：没想到**左子树为空**时 `l_min` 是哨兵 `inf`。
- **讲解过程**：
  1. **三种少返回值的写法**（都用 20000 棵随机树对拍过）：
     - 写法 1：返回 `(min, max)`，「是否合法」交给 `self.ok`（分解 + 外部变量）
     - 写法 2：合法返回 `(min, max)`，不合法返回 `None`（像二分「没找到返回 -1」，还能提前停）
     - 写法 3（最简单）：**BST 中序严格递增**，记住上一个值 `self.prev`，一个值都不返回：
       ```python
       def inorder(node):
           if node is None or not self.ok:
               return
           inorder(node.left)
           if self.prev is not None and node.val <= self.prev:
               self.ok = False
           self.prev = node.val
           inorder(node.right)
       ```
  2. **`min(l_min, node.val)` 的原因**：合法且左子树非空时，`l_min` 确实更小；但左子树为空时，空节点返回的 `l_min = inf`：
     | 情况 | `l_min` | `min(l_min, node.val)` |
     |---|---|---|
     | 左子树非空 | 左子树最小值 | `l_min` |
     | 左子树为空 | `inf`（哨兵） | `node.val` |
     相当于 `l_min if node.left is not None else node.val` 的统一写法。右边 `max(r_max, node.val)` 同理。
  3. **空节点为什么返回 `(True, inf, -inf)`**：比较时 `-inf < node.val < inf` 永远成立；往上交时 `min(inf, x)`、`max(-inf, x)` 自动选 x。换成 `(True, 0, 0)`：叶子 5 会算 `0 < 5 < 0` → 误判不合法；负数节点 `min(0, -3)` 交上去一个树里不存在的 0。
  4. **哨兵**：选一个不影响任何比较和计算的初始值（`best = -inf`、`dummy` 同一个思路），空的情况就不用单独写 `if`。
- **结论**：空子树返回 `inf` / `-inf` 是哨兵，`min(l_min, node.val)` 是为了在左子树为空时把哨兵换成自己的值。
- **待办**：
  - 检验题未答：树 `5(左 3)`，节点 3 交上来 `(True, 3, 3)`，节点 5 返回什么？（`(True, 3, 5)`：右边空 `r_min = inf`，`3 < 5 < inf` 成立；min(3, 5) = 3；max(-inf, 5) = 5）
  - 检验题未答：写法 3 为什么用 `<=` 而不是 `<`？（BST 要求严格递增，`[2, 2, 2]` 不合法，相等也要判 False）
- **关联**：Q54、Q61（96 空树返回 1 也是哨兵）、Q32 / Q50（`-inf` 初始值）

#### Q56 · 验证 BST 算动态规划吗？
- **时间**：2026-11-11 17:56
- **原始问题**：「算是动态规划吗？」
- **卡点**：把「分解问题」和「动态规划」画了等号。
- **讲解过程**：
  1. **DP = 分解问题 + 重叠子问题 + 备忘录**。斐波那契里 `fib(3)` 被算多次，存下来就从指数降到 O(n)。
  2. 树里**每棵子树只有一个父节点**，每个子问题只被调用一次，没有重叠 → 不需要备忘录，叫**分治 / 递归**。
     | | 验证 BST | 斐波那契 / 爬楼梯 |
     |---|---|---|
     | 思路 | 分解 | 分解 |
     | 同一子问题算几次 | 1 次 | 很多次 |
     | 备忘录 | 不用 | 要 |
     | 叫法 | 分治 | 动态规划 |
  3. **树形 DP**（如 337 打家劫舍 III）：一棵子树也只算一次，但在「抢 / 不抢」多个状态间求最优，习惯叫 DP。后序版 `(ok, min, max)` 结构很像，但 98 是判断题不是最优化，一般不这么叫。
  4. 真正有重叠的树题：96 不同的 BST（见 Q61）。
- **结论**：分解问题不一定是 DP；有**重叠子问题**并用备忘录消掉重复，才是 DP。
- **待办**：检验题未答：画 `f(4) = f(3) + f(2)` 的递归树，哪些子问题被算了不止一次？（`f(2)` 算 2 次，`f(1)` 算 3 次，`f(0)` 算 2 次）
- **关联**：Q54、Q61

#### Q57 · 末尾的 `return` 什么时候要写？能不能删掉 `return left and right`？DFS 就不需要 return 吗？
- **时间**：2026-11-11 18:07（追问 18:09、18:10，用户总结 19:05）
- **原始问题**：「能不能实现删除 `return left and right`」「DFS 就不需要 return」「主要是不写最后的 return 它也会自己弹栈啊」。用户最后总结：「不管什么遍历，最后的那个 return 不取决于遍历的种类，而是取决于我们要不要最后回传一个值，要回传值就要写，不用回传就不用写。」
- **卡点**：把「DFS」和「不返回值」绑在一起；把 `return` 理解成「让函数结束」。
- **讲解过程**：
  1. **直接删会怎样**：函数走到末尾自动返回 `None`（错题本 #9），合法的树最后返回 `None` → 被判成不合法；违规节点的 `return False` 交给父节点后也没人用。
  2. **改成遍历思想就能删**：`self.valid = True`，`return False` 换成 `self.valid = False; return`，所有 `return` 不带值，`left` / `right` 删掉，检查逻辑和参数**一行没变** → 再次证明它本质是遍历（Q54）。
  3. **DFS / BFS 和 return 是两个维度**：
     | | 不返回值（遍历） | 返回值（分解） |
     |---|---|---|
     | DFS | `self.valid` 版 98；带 depth 的最大深度 | `left and right` 版 98；`max(左, 右) + 1` |
     | BFS | 102 层序遍历 | 很少见 |
     「不返回值」≠「不写 `return`」：遍历写法仍需要空 `return` 来提前结束。
  4. **`return` 的作用不是弹栈**，函数执行完本来就会弹栈；`return x` 是「回去时交一份报告」：
     | `return` 的位置 | 作用 |
     |---|---|
     | 中途 `if ...: return` | 提前结束，跳过后面的代码（如 None 检查） |
     | 末尾 `return x` | 把结果交给父节点 |
     | 末尾不带值 | 可省略 |
  5. **用户的总结完全正确**，再补一条：**一旦决定回传值，每一条执行路径都必须回传有意义的值**（700 searchBST 的 bug 就是有路径没值，见 Q58）。写带返回值的递归：① 先写定义（返回什么）；② 逐条检查每个出口是否按定义交出东西。
- **结论**：末尾的 `return x` 只取决于父节点需不需要这个值，和前 / 中 / 后序、DFS / BFS 都无关；要回传就每条路径都回传。
- **待办**：检验题未答：`countNodes`（`return countNodes(left) + countNodes(right) + 1`）是 DFS 还是 BFS？遍历还是分解？（DFS；分解：父节点必须拿到子树的个数）
- **关联**：Q54、Q58、Q60；错题本 #9；→ 错题本 #47

#### Q58 · LeetCode 700 二叉搜索树中的搜索：`UnboundLocalError`
- **时间**：2026-11-11 19:00
- **原始问题**：贴出代码（未附文字）：
  ```python
  def traverse(self, root: Optional(TreeNode), val: Optional(int)) -> Optional(TreeNode):
      if root is None:
          return None
      if root.val == val:
          return root
      if root.val > val:
          left = self.traverse(root.left, val)
      if root.val < val:
          right = self.traverse(root.right, val)
      return left if left else right
  ```
  （注释里还留着两边都搜的旧版本。）
- **卡点**：从「两边都搜」改成「只走一边」后，沿用了旧版最后一行。
- **讲解过程**：
  1. 思路对：利用左小右大只走一边，O(N) → O(树高)。
  2. 本地用 `[4, 2, 7, 1, 3]` 跑：找 2、1 成功；找 7 → `UnboundLocalError: cannot access local variable 'left'`；找 5（不存在）→ `... 'right'`。
  3. 原因：两个 `if` 只执行一个，另一个变量**从未赋值**。找 7：根 4 只赋值了 `right`，最后一行先读 `left` 就崩；找 5：在节点 7 只赋值了 `left = None`，假值 → 去读 `right` → 崩。旧版两边都搜，两个变量都一定有值，所以那一行在旧版里能用。
  4. 改法提示：每个分支直接 `return self.traverse(...)`，不再需要 `left` / `right`；`searchBST` 只是原样转调，可以直接递归自己。
  5. `val: Optional(int)`：val 不可能是 None，应写 `val: int`；圆括号第 5 次。
- **结论**：带返回值的递归，每条路径都要有值；只走一边时，在分支里直接 `return` 子问题的结果。
- **待办**：用户还没贴出修正版。参考：
  ```python
  def searchBST(self, root, val):
      if root is None or root.val == val:
          return root
      if root.val > val:
          return self.searchBST(root.left, val)
      return self.searchBST(root.right, val)
  ```
- **关联**：Q57；→ 错题本 #48

#### Q59 · 如何用递归获得 BST 的最小节点？
- **时间**：2026-11-13 13:36
- **原始问题**：「如何用递归的方式获得 BST 的最小节点？」
- **卡点**：无，新知识点。
- **讲解过程**：
  1. 左子树都比根小 → 一直往左走，走到**没有左孩子**的节点就是最小值。
  2. 两步法：定义「返回以 root 为根的子树里最小的节点」；出口：没有左孩子 → 返回自己；有左孩子 → `return self.getMin(root.left)`（`return` 不能省，否则交回 None）。
     ```python
     def getMin(self, root):
         if root is None or root.left is None:
             return root
         return self.getMin(root.left)
     ```
  3. 不用看右子树，只有一条路径，O(树高)。这是尾递归，可改成循环 `while root.left: root = root.left`。
  4. 用途：450 删除有两个孩子的节点时，用右子树最小值（后继）顶替。
- **结论**：BST 最小值 = 最左边的节点；递归每个出口都要 `return`。
- **待办**：检验题未答：写出 `getMax`，在树 `5(3(2(1), 4), 8)` 里依次经过哪些节点？（`return self.getMax(root.right)`；经过 5 → 8）
- **关联**：Q58、Q60

#### Q60 · LeetCode 450 删除 BST 中的节点：为什么超出内存限制？
- **时间**：2026-11-13 13:47（「没听懂」13:48，修改版 13:51）
- **原始问题**：贴出代码和 MLE 截图（未附文字）：
  ```python
  def deleteNode(self, root, key):
      if root is None:
          return None
      if root.val < key:
          root.right = self.deleteNode(root.right, key)
      if root.val > key:
          root.left = self.deleteNode(root.left, key)
      # 找到 node，删除
      if root.left is None:
          return root.right
      if root.right is None:
          return root.left
      if root.left is not None and root.right is not None:
          target = self.getMin(root.right)
          self.deleteNode(root.right, target.val)
          target.left = root.left
          target.right = root.right
          root = target
          return root
  ```
- **卡点**：① 往下递归之后没停，继续掉进「删除自己」的逻辑；② 调用 `deleteNode` 时没接住返回值；③ 改版后末尾没有 `return root`。
- **讲解过程**：
  1. 本地加打印跑示例（删 3）：`visit 5 → visit 3 (treat 3 as found, target 4) → visit 4 → treat 5 as found!`，最后 `4.right is 4` 为 True，树里有环，LeetCode 转列表时无限走 → MLE。
  2. **Bug 1（掉下去）**：在节点 5，`5 > 3` 去左边删完 3 后，代码继续往下，把 5 当成要删的节点又删了一遍。三种情况（往右 / 往左 / 就是我）**互斥**，用 `if / elif / else`；往左右删完后当前节点不变，`return root`。
  3. **Bug 2（丢返回值）**：`self.deleteNode(root.right, target.val)` 的结果没接住。删 3 时右子树只有 4，删掉后应返回 None，但 `root.right` 还是 4 → `target.right = root.right` 变成 `4.right = 4` → 环。`deleteNode` 是靠**返回值**交回新子树，不会原地改，必须写 `root.right = self.deleteNode(...)`（和自己第 19、21 行一样）。
  4. **用户修改版**加了 `elif`，Bug 1 修好了；但左右分支走完后函数到末尾自动返回 None → 根节点返回 None，整棵树丢了，需要在最后补 `return root`。Bug 2 仍未改。
  5. 小问题：`getMin` 注解 `Optional(...)` 第 6 次；前两个 `if` 已排除单孩子，最后那个 `if ... and ...` 一定成立，可删。
- **结论**：「在子树里删除，返回新的根」这种定义下：三种情况互斥；每条路径都 `return`；调用自己时一定要接住返回值。
- **待办**：用户还没贴出最终版。参考：
  ```python
  def deleteNode(self, root, key):
      if root is None:
          return None
      if root.val < key:
          root.right = self.deleteNode(root.right, key)
      elif root.val > key:
          root.left = self.deleteNode(root.left, key)
      else:
          if root.left is None:
              return root.right
          if root.right is None:
              return root.left
          target = self.getMin(root.right)
          root.right = self.deleteNode(root.right, target.val)
          target.left = root.left
          target.right = root.right
          return target
      return root
  ```
- **关联**：Q57、Q58、Q59；→ 错题本 #49

#### Q61 · LeetCode 96 不同的二叉搜索树：代码怎么想的？base case 为什么返回 1？
- **时间**：2026-11-13 15:35（追问 15:46）
- **原始问题**：贴出 `count(lo, hi)` 版代码和题图：「这个代码怎么想的，我看都看不懂，能不能从我们已经学过的模版出发？」追问：「我还是没看懂这个 base case。」
  ```python
  def numTrees(self, n):
      return self.count(1, n)
  def count(self, lo, hi):
      if lo > hi:
          return 1
      res = 0
      for i in range(lo, hi + 1):
          left = self.count(lo, i - 1)
          right = self.count(i + 1, hi)
          res += left * right
      return res
  ```
- **卡点**：整体思路；尤其「没有数字时为什么是 1 种，而不是 0 种」。
- **讲解过程**：
  1. **定义**（分解问题）：`count(lo, hi)` = 用 `lo..hi` 能组成多少种 BST；答案是 `count(1, n)`。范围 `(lo, hi)` 和 98 传参同一个想法。
  2. **for 挨个试谁当根**（回溯框架里的「逐个尝试选择」）。
  3. **左小右大把数字分两段**：左子树用 `[lo, i-1]` → `count(lo, i-1)`，右子树用 `[i+1, hi]` → `count(i+1, hi)`；相信递归。
  4. **乘法原理**：左 2 种 × 右 2 种 = 4 种（2 件上衣 × 2 条裤子）；外层把每个根的种数加起来。
  5. **base case 倒推**：n = 1 时 `count(1,1)` 只能 1 当根，`left = count(1,0)`、`right = count(2,1)` 都是空。答案必须是 1 → `left * right = 1` → base case 只能返回 1；返回 0 会得到「一个节点能组成 0 种树」。
     - `count` 数的是**摆法**，不是节点数：空子树有 0 个节点，但有 1 种摆法（空着）。
     - 类比：2 件上衣、0 顶帽子 → 2 套（不戴也是一种选择），不是 2 × 0 = 0 套。
     - 0 只表示「不可能」，而把 0 个数摆成空树是可能的。
     - 和 98 的 `inf` / `-inf` 同一个思路：乘法里不破坏结果的值是 1，加法里是 0。
  6. **走一遍 n = 3**：根 1：1 × 2 = 2；根 2：1 × 1 = 1；根 3：2 × 1 = 2；合计 5 ✅
  7. **这题才是真正的 DP**：`count(1, 2)` 等子问题被重复调用 → 加备忘录 `self.memo[(lo, hi)]`，分解 + 重叠子问题 + 备忘录 = 动态规划。
     | 用到的旧知识 | 在这题里的作用 |
     |---|---|
     | 分解问题：先写定义 | `count(lo, hi)` 的含义 |
     | 回溯：for 挨个尝试 | 每个数轮流当根 |
     | 98 的范围 (lo, hi) + 左小右大 | 根把数字分两段 |
     | 哨兵 | 空树返回 1 |
     | 重叠子问题 → 备忘录 | 变成 DP |
- **结论**：每个数轮流当根，左右种数相乘再求和；空树算 1 种摆法（乘法的中性元素）；有重叠子问题，加备忘录就是 DP。
- **待办**：
  - 检验题未答：算 `count(1, 2)`。（根 1：`count(1,0) × count(2,2)` = 1 × 1 = 1；根 2：`count(1,1) × count(3,2)` = 1 × 1 = 1；合计 2，确实只能画出 2 种）
  - 检验题未答：`count(1, 2)` 和 `count(4, 5)` 一样吗？结果只和什么有关？（一样，只和数字个数 `hi - lo + 1` 有关 → 可以改成 `count(k)`，即卡特兰数）
- **关联**：Q54、Q55、Q56、Q51（回溯 for 尝试）→ 错题本 #50

#### Q62 · 图的邻接表：`Edge` 只存了终点，起点和 weight 属于哪条边怎么知道？
- **时间**：2026-11-13 17:18
- **原始问题**：看加权有向图的邻接表实现（`class Edge: to, weight`；`self.graph = [[] for _ in range(n)]`；`addEdge` 里 `self.graph[from_].append(self.Edge(to, weight))`）：「这个 Edge 只提供了一个终点，但没有说明起点，那这个 weight 是哪个，怎么知道呢？」
- **卡点**：没注意到 Edge 被放进了 `graph[from_]`。
- **讲解过程**：
  1. 起点就是 Edge 所在格子的**下标**：
     ```
     graph[0] → [Edge(to=1, w=5), Edge(to=2, w=3)]   # 0 出发的所有边
     graph[1] → [Edge(to=2, w=7)]
     graph[2] → []
     ```
     「`graph[0]` 里有 `Edge(1, 5)`」= 从 0 到 1、权重 5。
  2. 不存 `from` 是因为会重复：拿到一条边一定是先去 `graph[x]` 里找，那时已经知道起点是 x（`for e in self.graph[0]: print(0, e.to, e.weight)`）。类比：张三的通讯录页面里只写「李四，认识 5 年」。
  3. 本质和 dict 一样：key = 起点，value = 出边列表；节点是 0..n-1 时用 list 下标代替 key（注释里的 `Map<Integer, List<Edge>>` 就是 dict 版）。
- **结论**：邻接表里边的起点由「它在哪个列表里」决定，Edge 只需存终点和权重。
- **待办**：检验题未答：`removeEdge` 里为什么只检查 `e.to != to`？（遍历的是 `graph[from_]`，里面所有边起点都是 `from_`）
- **关联**：Q35（dict / 哈希表）、Q63

#### Q63 · `visited` 和 `onPath` 有什么区别？「s 被标记为 visited 就剪枝」是什么意思？跟环有什么关系？
- **时间**：2026-11-13 17:36（追问 17:38、17:40）
- **原始问题**：看「同时使用 visited 和 onPath 数组」一段：「这里对 s 的解释是什么意思？」追问：「这跟环有什么关系？」「所以检测到 visited 之后，就可以跳过？」
- **卡点**：分不清两个数组各管什么；以为碰到 visited 一律跳过。
- **讲解过程**：
  1. 两个数组：
     | 数组 | 何时设 True | 何时撤销 | 含义 |
     |---|---|---|---|
     | `onPath[s]` | 进入 s | 离开 s 时设回 False | s **现在**在当前路径（递归栈）上 |
     | `visited[s]` | 进入 s | 永不撤销 | s **曾经**被访问过 |
     `onPath` 就是回溯的「做选择 → 递归 → 撤销」。
  2. 判环代码（顺序：先 onPath 后 visited）：
     ```python
     def traverse(s):
         if onPath[s]:          # 走回当前路径上的节点 → 有环
             has_cycle = True
             return
         if visited[s]:         # 以前完整查过、不在当前路上 → 剪枝
             return
         visited[s] = True
         onPath[s] = True
         for e in graph[s]:
             traverse(e.to)
         onPath[s] = False
     ```
  3. **环 = 走回了当前路径上的节点**，只有 `onPath` 能判断。例：`0→1→2→0`，走到 2 → 0 时 `onPath[0]` 为 True → 有环。
  4. **只看 visited 判断不了**：`0→1→2, 0→2` 没有环，但第二次走到 2 时它也 visited 了，那只是两条路**汇合**。
     | 碰到访问过的 s | `onPath[s]` | 意思 |
     |---|---|---|
     | 还在当前路上 | True | 有环 |
     | 不在当前路上 | False | 汇合，s 往下早查完 → 剪枝 |
  5. **为什么能剪枝**：DFS 是先把 s 下面的路全走完才撤销 `onPath[s]`，所以「visited 且不在路上」= s 往下全部查过。当时没发现环，再走一遍结果也一样（s 往后的路是固定的）。和备忘录同理：只是不存数字，只记「查过了，没问题」。
  6. **「visited 就跳过」要加前提**：在当前路径上的节点也是 visited 的。先查 visited 的话，`0→1→2→0` 走回 0 时直接 return，环就漏了。
- **结论**：`onPath` 回答「有没有环」，`visited` 回答「还用不用再查」；visited 且不在路上 → 跳过，还在路上 → 有环。
- **待办**：检验题未答：自环 `0 → 0` 能被检测出来吗？（能：进入 0 时 `onPath[0] = True`，遍历出边又到 0，第一行就判出有环）
- **关联**：Q51（回溯撤销）、Q61（备忘录）、Q62；→ 错题本 #52

#### Q65 · Union-Find 路径压缩：为什么摊还分析是 O(1)？极端情况下不是 O(N) 吗？
- **时间**：2026-11-18 14:42
- **原始问题**：看 labuladong 第二种路径压缩（递归版 `find`：`self.parent[x] = self.find(self.parent[x])`，一次把整条树枝压平）：「这样子写 find 算法，为什么摊销分析出来是 O(1)？如果极端情况下不是会 O(N) 嘛？」
- **卡点**：把「单次最坏」和「摊还（平均）」当成一回事。
- **讲解过程**：
  1. 单次 `find` 最坏确实 O(N)。摊还说的是「**很多次加起来，平均每次**很快」。
  2. 例子：长度 N 的链，连续 N 次 find：第 1 次走 N 步，顺手把路上所有节点挂到根上；之后每次 1 步 → 总 ≈ 2N，平均 ≈ 2。
  3. **高树不会白白出现**：想再造一条长度 N 的链，要先做约 N 次 union。每次昂贵的 find 之前，都有很多便宜的操作在「攒钱」。类比：每天存 1 块，第 30 天一次花 30 块，平均每天 1 块。
  4. 严谨的结论：
     | 优化 | 摊还复杂度 |
     |---|---|
     | 无 | 单次最坏 O(N) |
     | 只做路径压缩 | O(log N) |
     | 路径压缩 + 按秩 / 按大小合并 | O(α(N)) |
     α 是反阿克曼函数，N 等于宇宙原子数时也不超过 4，实际中当 O(1)。labuladong 说的 O(1) 是简化说法（和错题本 #38 一样，O 不是等式）。
- **结论**：路径压缩让一次昂贵的 find 把树压平，代价被摊到前后很多次便宜操作上，平均接近常数。
- **待办**：检验题未答：对一条链调用递归版 `find(x)` 后，再 `find(x 的父节点)` 要几步？（1 步：路径上所有节点都已直接挂在根下）
- **关联**：Q43（O(log N) 不是公式）、Q67、Q71；错题本 #38

#### Q67 · LeetCode 130 被围绕的区域（Union-Find）：35/59 通过，哪里错？
- **时间**：2026-11-18 16:16
- **原始问题**：贴出用 Union-Find 的代码和失败用例截图（未附文字）。思路：边界上的 `O` 连到 dummy（`m*n`），内部相邻的 `O` 互相 union，最后内部不和 dummy 连通的改成 `X`。`UF.connected` 写成：
  ```python
  def connected(self, p, q):
      rootP = self.parent[p]
      rootQ = self.parent[q]
      ...
  ```
- **卡点**：用 `parent` 代替了根。
- **讲解过程**：
  1. 本地跑失败用例：被误改成 `X` 的格子 `(1, 2)`，`parent` 是 7、`find` 得到的根是 28；dummy 的根也是 28 → 其实连通，但 `connected` 比的是 parent，判成不连通。
  2. 判断连通要比**根**；`parent[p]` 不一定是根，路径压缩只在调用 `find` 时发生，没被 find 过的节点 parent 可能还指着中间节点。和 `union` 里写的 `self.find(p)` 对照即可。
  3. 样例 1 能过是因为树很矮，parent 碰巧是根（「碰巧对」）。
  4. 小点：`return rootP == rootQ` 即可；内层循环 `i` 只取 `1..m-2`，`x = i + dx` 不会越界 ✅
- **结论**：并查集里判断连通 = 比较 `find` 出来的根，不是比较 parent。
- **待办**：用户还没贴出修正版（改成 `return self.find(p) == self.find(q)`）。
- **关联**：Q65、Q66；→ 错题本 #54

#### Q68 · 树和无环无向图有什么区别？261 以图判树能不能只判断有没有环？
- **时间**：2026-11-18 16:43
- **原始问题**：看 261「以图判树」：「树和没有环的无向图有啥区别，能不能直接通过判断它有没有环？」
- **卡点**：漏了「连通」这个条件。
- **讲解过程**：
  1. **树 = 无环 + 连通**。反例：`n = 4, edges = [[0,1], [2,3]]` 无环但分成两块（森林）；`n = 3, edges = [[0,1]]` 有孤立点 2。
     | | 无环 | 连通 |
     |---|---|---|
     | 树 | ✅ | ✅ |
     | 森林（无环无向图） | ✅ | 不一定 |
     | 连通图 | 不一定 | ✅ |
  2. Union-Find 两个条件都判：
     ```python
     for u, v in edges:
         if uf.connected(u, v):   # 已经连通，再加这条边就成环
             return False
         uf.union(u, v)
     return uf.count() == 1       # 最后只剩一个连通分量
     ```
  3. 性质：n 个节点的图，「连通」「无环」「恰好 n − 1 条边」任意满足两个 → 第三个也成立 → 是树。
- **结论**：判断树要同时判无环和连通（或用 n − 1 条边代替其中一个）。
- **待办**：检验题未答：`n = 4, edges = [[0,1], [1,2], [2,0]]` 是树吗？满足哪几个条件？（不是；有 n − 1 条边，但有环、节点 3 不连通）
- **关联**：Q63（有向图判环）、Q71（Kruskal 判环）

#### Q71 · LeetCode 1584 连接所有点的最小费用（Kruskal）：哪里错？
- **时间**：2026-11-18 18:52
- **原始问题**：贴出代码（未附文字）：建所有点对的曼哈顿距离边、按距离排序、UF 判环累加。`UF.find` 写成：
  ```python
  def find(self, x):
      if x == self.parent[x]:
          return
      self.parent[x] = self.find(self.parent[x])
      return self.parent[x]
  ```
- **卡点**：base case 的 `return` 没带值。
- **讲解过程**：
  1. 引导代入：初始 `parent[i] == i` → `find(i)` 返回 None，`find(j)` 也是 None → `connected` 里 `None == None` 为 True → 所有边都 `continue` → `mst = 0`。
  2. `find` 的定义是「返回 x 的根」，base case 这条路径没交出根（和错题本 #48、#49 同类：每条路径都要按定义返回）。应为 `return x`。
  3. 小点：`if ...: continue` 后面不用写 `else`。
- **结论**：带返回值的函数，base case 也必须按定义返回值；`return` 不带值 = 返回 None。
- **待办**：用户没回复 4 个引导问题，也没贴修正版。
- **关联**：Q57、Q65、Q68；→ 错题本 #55

#### Q72 · LeetCode 654 最大二叉树：超出时间限制
- **时间**：2026-11-19 15:52
- **原始问题**：贴出代码和 TLE 截图（未附文字）：
  ```python
  maxIndex = nums.index(maxValue)
  left = self.constructMaximumBinaryTree(nums[:maxIndex])
  right = self.constructMaximumBinaryTree(nums[maxIndex:n])
  ```
- **卡点**：右边的切片把最大值本身也带了进去。
- **讲解过程**：
  1. 代入 `[3,2,1,6,0,5]`：`maxIndex = 3`，`right = nums[3:6] = [6,0,5]`，6 已经当了根却还在右子树里；对 `[6,0,5]` 再递归，right 还是 `[6,0,5]` → 问题不缩小 → 无限递归（本地是 `RecursionError`）。
  2. 应为 `nums[maxIndex+1:]`。和错题本 #4、#19 同类：切片开闭区间。
  3. **递归检查清单**再加一条：每次递归，问题规模必须严格变小。
  4. 小点：`nums[x:]` 可省略 n；`if not nums:` 更直接；切片 + max + index 最坏 O(N²)，更省的写法是传 `(lo, hi)` 下标（同 96、98 的思路）。
- **结论**：根已经用掉了，左右子树的区间都不能再包含它。
- **待办**：用户还没贴出修正版。
- **关联**：Q61（传范围）、Q75；→ 错题本 #56

#### Q74 · 二叉树 `find`：最后为什么要 `return left if left is not None else right`？这是怎么想出来的？
- **时间**：2026-11-20 11:35（追问 11:38、11:40）
- **原始问题**：看 labuladong 的 LCA 前置 `find` 函数（先左右递归，后序位置判断 `root.val == val` 就 `return root`，最后 `return left if left is not None else right`）：「我不懂为什么最后要这一行……如果左右子树都没有，那么没有什么意义吧，直接弹栈向上再搜索不是吗？我觉得这个不用写。」追问：「我还是不懂为什么要返回左右子树，这咋想出来的。」
- **卡点**：以为节点自己不是目标就不需要 return；把「返回孩子的结果」理解成「返回左右子树本身」。
- **讲解过程**：
  1. 函数定义：在以 root 为根的子树里找 val，**找到就把节点交上去**，找不到交 None。找到的节点要一层层传回最顶层。
  2. 代入 `1(2(4), 3)` 找 4：`find(4)` 返回节点 4 → `find(2)` 的 left 是节点 4，自己不是目标，转交节点 4 → `find(1)` 也转交 → 最终答案。删掉最后一行，`find(2)` 自动返回 None，答案在半路丢了。「弹栈」会发生，但带回去的是 None。
  3. 一行处理三种情况：left 找到 → left；只有 right 找到 → right；都没有 → right 本身就是 None。
  4. **从零想**：答案只可能在三处：自己、左子树、右子树。自己看一眼；左右子树看不见，只能派人问（递归）；拿到三份信息后按顺序交：
     ```python
     if root.val == val: return root
     if left is not None: return left
     if right is not None: return right
     return None
     ```
     原代码最后一行就是后三行的压缩。类比：CEO 找小王 → 问经理 → 经理问组长 → 组长找到了，经理必须转告 CEO。
  5. 和 700（错题本 #48）对比：这里 `left`、`right` 都无条件赋值，所以最后一行能用；700 只搜一边，另一个变量不存在才崩。
- **结论**：节点自己不是目标时，也要把孩子找到的结果原样转交上去；「返回左右子树」= 转交孩子交上来的节点。
- **待办**：检验题未答：树里有两个节点都等于 val，一个在左子树、一个在右子树，函数交回哪个？（左边那个：`left is not None` 先判断）
- **关联**：Q57（末尾 return = 带值回去）、Q58；→ 错题本 #58

#### Q75 · LeetCode 106 从中序与后序遍历构造二叉树：两个下标问题，改 base case 又改反了
- **时间**：2026-11-20 15:44（第二版 15:57）
- **原始问题**：贴出代码（未附文字），闭区间 `[start, end]`：
  ```python
  if postStart >= postEnd:
      return None
  ...
  num_of_left = rootIndex - inStart + 1
  ```
  第二版把 `num_of_left` 改对，base case 改成 `if postStart >= postEnd: return TreeNode(postorder[postEnd])`。
- **卡点**：闭区间里「1 个元素」和「0 个元素」的条件分不清。
- **讲解过程**：
  1. 本地跑示例 `inorder = [9,3,15,20,7]`、`postorder = [9,15,7,20,3]`：原代码 `RecursionError`；只修 base case → `[3, null, 20]`（叶子丢了）；两个都修 → 正确。
  2. **`num_of_left` 多 1**：第一层 `inStart = 0`、根 3 的 `rootIndex = 1`，左边只有 1 个数，`1 - 0 + 1 = 2` 多算 → 左子树把根也分进去，规模不缩小 → 无限递归（和 654 同一现象）。应为 `rootIndex - inStart`。
  3. **base case 把单元素当空**：闭区间 `postStart == postEnd` 时有 1 个元素，应建节点；`>=` 把所有叶子扔掉。
  4. **第二版改反了**：`>=` 同时包含 `==`（1 个元素）和 `>`（0 个元素），全部建节点 → 空区间也建了节点。反例 `inorder = [1,2]`、`postorder = [1,2]`，正确 `[2, 1]`，输出 `[2, 1, 1]`：右子树 `post[1..0]` 是空的，却建了 `TreeNode(post[0] = 1)`。示例 1 没有「只有一个孩子」的节点，所以碰巧过了。
  5. 正确：`if postStart > postEnd: return None`；单元素不用单独写，照常走下去，左右都会变成空区间。
  6. 小点：`value_to_index = {}` 是类变量（错题本 #40 同坑），应在入口里 `self.value_to_index = {}`；`Optional(TreeNode)` 圆括号第 7 次。
- **结论**：闭区间 `[s, e]`：空 ⇔ `s > e`，单元素 ⇔ `s == e`；base case 写**真正为空**的条件。
- **待办**：用户还没贴出最终版。
- **关联**：Q61、Q72、Q76；错题本 #4、#40；→ 错题本 #59、#60

#### Q76 · LeetCode 889 根据前序和后序遍历构造二叉树：缺参数 + 缺单元素 base case；只要不越界就没事吗？
- **时间**：2026-11-20 19:37（追问 19:43、19:45，逐步分析 19:49）
- **原始问题**：贴出代码（未附文字），这次用左闭右开 `[start, end)`：
  ```python
  if preStart >= preEnd:
      return None
  rootValue = preorder[preStart]
  leftRootValue = preorder[preStart+1]
  leftRootIndex = self.value_to_index[leftRootValue]
  num_of_left = leftRootIndex - postStart + 1
  left = self.build(preorder, preStart+1, preStart+num_of_left+1, postorder, postStart, leftRootIndex+1)
  right = self.build(preorder, preStart+num_of_left+1, postorder, leftRootIndex+1, postEnd-1)
  ```
  追问：「是不是只有测试用例本身只有一个元素时才错？不是的话我这个应该是对的？」「主要还是数组越界了，不然我也不用担心这个条件，对吧？」「以 Example 1 为例，能不能逐步分析？」
- **卡点**：① `right` 调用漏了 `preEnd`；② 没有单元素 base case；③ 以为单元素问题只是「越界」。
- **讲解过程**：
  1. 进步：左闭右开 + `>=` 的 base case 一致；注解用了 `Optional[TreeNode]` 方括号 ✅；`num_of_left` 和各段区间都对。
  2. 本地跑示例：原代码 `IndexError`；只补参数仍 `IndexError`；再加单元素 base case → 正确。
  3. **每个用例都会碰到单元素区间**：任何树都有叶子，递归一定走到叶子。叶子 4 的区间 `pre[2:3]`，读 `preorder[3] = 5`（兄弟），算出 `num_of_left = 2`，左子树区间 `pre[3:5] = [5, 3]` 越出了父节点的范围——**没报错但逻辑已错**；最后叶子 7 读 `preorder[7]` 才越界。
  4. **越界只是症状**：代码的假设「`preorder[preStart+1]` 是左子树的根」只在区间至少 2 个元素时成立。写 base case 要问「下面的代码依赖哪些假设？什么时候不成立？」而不是「什么时候会崩」。报错其实是在帮你暴露 bug。
  5. **逐步分析**（正确代码，post 位置表 4→0, 5→1, 2→2, 6→3, 7→4, 3→5, 1→6）：
     | 层 | 区间 | 根 | 左根 / 位置 | 左子树个数 | 左 / 右区间 |
     |---|---|---|---|---|---|
     | 1 | pre[0:7] | 1 | 2 / 2 | 3 | pre[1:4] post[0:3] / pre[4:7] post[3:6] |
     | 2 左 | pre[1:4] | 2 | 4 / 0 | 1 | [4] / [5] |
     | 2 右 | pre[4:7] | 3 | 6 / 3 | 1 | [6] / [7] |
     | 3 | [4] [5] [6] [7] | 单元素 base case 直接建节点 | | | |
     核心：pre 第一个是根、第二个是左子树的根；在 post 里左子树的根是左子树最后一个，由它的位置得到左子树大小。
  6. 和 106 对比：106 单元素不用单独处理（会自然走到空区间）；889 的逻辑要读「第二个元素」，单元素时没有，必须单独拦住。
- **结论**：889 需要两个 base case：空区间返回 None，单元素返回 `TreeNode(preorder[preStart])`；递归只能读自己区间里的数据。
- **待办**：用户还没贴出修正版。参考：
  ```python
  if preStart >= preEnd:
      return None
  if preEnd - preStart == 1:
      return TreeNode(preorder[preStart])
  ...
  right = self.build(preorder, preStart+num_of_left+1, preEnd, postorder, leftRootIndex+1, postEnd-1)
  ```
- **关联**：Q75、Q61；→ 错题本 #61、#62

#### Q77 · LeetCode 70 爬楼梯（备忘录）：n = 4 起 `IndexError`
- **时间**：2026-11-23 15:14
- **原始问题**：贴出代码（未附文字）：入口 `climbStairs` 建 `self.dp = [-1]*(n+1)` 再调 `self.__climbStairs(n)`；辅助函数里写的是 `self.dp[n] = self.climbStairs(n-1) + self.climbStairs(n-2)`。
- **卡点**：辅助函数递归时调用了入口函数。
- **讲解过程**：
  1. 本地：n = 3 → 3 ✅；n = 4、5 → `IndexError: list assignment index out of range`。
  2. 代入 n = 4：入口建长度 5 的 dp → 辅助函数调 `climbStairs(3)` → 入口又执行 `self.dp = [-1]*4`，dp 被换成长度 4 的新列表 → 回到外层写 `self.dp[4]` 越界。备忘录也被反复清空。
  3. n = 3 能过：它调用的 `climbStairs(2)`、`climbStairs(1)` 在第一行就 return，没重建 dp（「碰巧对」）。
  4. 和错题本 #43（543 递归调了入口函数）完全同一个错误，第 2 次。入口只调用一次负责初始化，**递归只调辅助函数**。
  5. 小点：`__init__` 里的 `self.dp = []` 用不到；双下划线方法名会触发 name mangling，辅助方法一般用单下划线 `_helper`。
- **结论**：入口函数初始化、辅助函数递归，递归调用要写辅助函数的名字。
- **待办**：用户还没贴出修正版（改成 `self.__climbStairs(n-1) + self.__climbStairs(n-2)`）。
- **关联**：Q50（543）、Q56、Q61（备忘录）；→ 错题本 #63

#### Q79 · 两种二分写法的边界为什么不一样？（`left_bound` 闭区间 vs LIS 左闭右开）怎么看出 `right` 是「下一格」？
- **时间**：2026-11-23 16:31（追问 16:33）
- **原始问题**：对比 `left_bound`（`right = len(nums) - 1`、`while left <= right`、`right = mid - 1`）和 300 LIS 牌堆的二分（`right = piles`、`while left < right`、`right = mid`）：「这两个的二分查找的边界为什么不一样？怎么判断边界啊，一个是 mid 不包含，一个是 mid 包含一半，while 判断边界也不一样。」追问「最后一个位置的下一格」：「怎么判断出来的？」
- **卡点**：以为 `right = mid` 是「包含 mid」；不知道三处写法都由区间约定决定。
- **讲解过程**：
  1. **先定区间**：
     | | `left_bound` | LIS |
     |---|---|---|
     | 初始 `right` | `len - 1`（最后一个下标） | `piles`（长度） |
     | 区间 | 闭 `[left, right]` | 左闭右开 `[left, right)` |
  2. **`while` = 区间不为空**：闭区间 `[3, 3]` 还有一个元素 → `left <= right`；开区间 `[3, 3)` 已空 → `left < right`。
  3. **两种写法每轮都排除了 mid**，只是表示不同：
     | 往哪边缩 | 闭区间 | 左闭右开 |
     |---|---|---|
     | 去掉右边（含 mid） | `right = mid - 1` | `right = mid` |
     | 去掉左边（含 mid） | `left = mid + 1` | `left = mid + 1` |
     `[left, mid)` 本来就不含 mid，所以 `right = mid` 不是「包含 mid」。
  4. **怎么看出「下一格」**：初始值是长度还是最后一个下标。长度 3 的数组下标 0、1、2，3 就是最后一格的下一格（同 `range(0, n)`）。`piles = 3` 时有效牌堆是 `top[0..2]`。代码也能验证：`left < right` 时 `mid = (left + right) // 2` 最多 `right - 1`，循环里从不读 `top[right]`；而 `left <= right` 允许 `mid == right`，所以闭区间的 right 必须能取到。
  5. **LIS 为什么用左闭右开**：找第一个 ≥ poker 的牌堆，都不合适就新建在 `piles` 处；`[0, piles)` 结束时 `left ∈ 0…piles`，`left == piles` 正好表示新建一堆。
  6. 一句话：先选区间，再按「区间里有什么」推出初始 `right`、`while` 条件、`right` 怎么缩；`left = mid + 1` 两种写法一样。和 106（闭区间）、889（左闭右开）的 base case 是同一件事。
- **结论**：初始值是 `len` → 开区间，`len - 1` → 闭区间；`while` 条件和收缩写法都由「空区间长什么样」决定。
- **待办**：检验题未答：把 `left_bound` 改成左闭右开，哪 3 处要改？（`right = len(nums)`；`while left < right`；`right = mid`）
- **关联**：Q26、Q29（二分边界、`mid ± 1`）、Q75、Q76（建树的区间约定）、Q80

#### Q80 · 为什么这样设计 `left` 就是左边界？找到 `==` 后收缩，后面再也没有 `==` 了怎么办？这个算法是怎么想出来的？
- **时间**：2026-11-23 16:38（追问 17:48、17:52、17:53、17:59，18:01 想通，18:14 自己推出右边界）
- **原始问题**：「为什么能搜索到左边界呢？如果查找到 ==，收缩边界，发现根本就没有 == 的了怎么办？」「我还是想不通为什么这样设计就能得到 left 是左边界的值呢」「二分查找找边界的算法是怎么想出来的」「（left 会自己走回最左边那个 2）为什么」「为什么能这么保证呢，我怎么没想出来」
- **卡点**：一直在**逐轮模拟**，情况太多，心里没底；**Q26 曾经学过同一个问题，这次又卡住**。
- **讲解过程**（换了 4 个角度，最后是第 ④ 个讲通的）：
  1. **走例子**：`[0, 1, 3, 5, 6]` 找 3：第 1 轮 mid = 2 命中，`r = 1` 把 3 也排除了；之后剩下的都 < 3，只有 `l` 在动：`l = 1`、`l = 2`，停在 2 ✅
  2. **是 / 否分界线**：把数组翻译成「`nums[i] >= target` 吗？」→ `否 否 是 是`，找第一个「是」。左闭右开时：「否」→ `left = mid + 1`；「是」→ `right = mid`（mid 保留为候选）。答案始终在范围里，缩到一个点就是答案。类比：一排灯泡前坏后好，找第一个好的。
  3. **怎么想出来的**：普通二分 `== 时 return mid` → 发现左边可能还有 → 改成 `right = mid - 1` 继续往左找（只改一行）→ 再抽象：只要条件「前面全否、后面全是」（单调）就能二分，左边界、LIS 牌堆、1011 二分答案是同一个模板。检查清单：区间开闭？mid 是还是否？答案始终在区间里？每轮都在缩小？
  4. **为什么 left 正好走回 p**：最左的 target 在 p，被排除后区间 `[left, p-1]` 全 < target → 只有 `left = mid + 1` 在动；`mid ≤ right = p - 1` → `left ≤ p`，不会越过；循环结束要 `left > p - 1` → 两边一夹 `left = p`。
  5. **循环不变量**（✅ 用户说「这个解释得很好，我想通了」）：不去模拟，只问「什么一直成立」：
     ```
     [ 全都 < target ][ left … right（还没看过）][ 全都 ≥ target ]
     ```
     ① `left` 左边全 < target（只有看到 `<` 才 `left = mid + 1`）；② `right` 右边全 ≥ target（看到 `>=` 才 `right = mid - 1`）。结束时中间为空 → `left` = 第一个 ≥ target。快排 partition、98 的 (lo, hi)、滑动窗口用的都是这个思路。二分 1946 年发表，第一个没 bug 的版本 1962 年才出现——想不出来很正常，要学的是怎么验证。
  6. **用户自己推出右边界** ✅：「`left = right + 1`，答案是 `right`，`left` 左边都 ≤ target，`right` 右边都 > target」。由此反推代码：`nums[mid] <= target` → `left = mid + 1`（`==` 动 left，和左边界相反）；否则 `right = mid - 1`；最后 `if right >= 0 and nums[right] == target`。
     | 版本 | 不变量 | 结束时 |
     |---|---|---|
     | 左边界（闭） | left 左 < t；right 右 ≥ t | left = 第一个 ≥ t |
     | 左边界（左闭右开） | left 左 < t；right **自己和**右边 ≥ t | left == right = 第一个 ≥ t |
     | 右边界（闭） | left 左 ≤ t；right 右 > t | right = 最后一个 ≤ t |
  7. target 不存在时 left 指向插入位置，要检查 `left < len(nums) and nums[left] == target`。
- **结论**：看不懂循环时别逐轮模拟，先找「每一轮结束时一定成立」的话（循环不变量），循环结束那一刻它就给出了答案。
- **待办**：检验题未答：`[2, 2, 2]` 找 2 逐轮走一遍，最后 left 是几？（mid = 1 → r = 0；mid = 0 → r = -1；结束 left = 0）
- **关联**：Q26（同一个问题第 2 次卡住）、Q29、Q79、Q49（partition 不变量）；→ 错题本 #65

#### Q81 · LeetCode 354 俄罗斯套娃信封：LIS 的二分死循环（超时）
- **时间**：2026-11-23 16:48
- **原始问题**：贴出代码（未附文字）：排序 + 取高度 + 牌堆 LIS，二分里 `mid = left + (right - left) // 2` 写在 `while` 外面。
- **卡点**：每轮要更新的量写在了循环外。
- **讲解过程**：
  1. 示例排序后高度 `[3, 4, 7, 4]`，处理最后一个 4：`left = 0, right = 3, mid = 1`；第 1 轮 `top[1] == 4` → `right = 1`；之后 `left < right` 一直成立，`mid` 还是 1，`right = 1` 不变 → 死循环。前几张牌碰巧一轮就收敛。
  2. 和错题本 #41（`cur = dq[0]` 写在 for 外面）同一个根源：赋值只在执行那一刻算一次，不会跟着 left / right 自动更新。
- **结论**：每一轮都要变的量必须写在循环里面。
- **待办**：用户还没贴出修正版（把 `mid = ...` 挪进 while 第一行）。
- **关联**：Q78（354 排序）、Q79、Q47（102 `cur`）；→ 错题本 #64

---

## 三、费曼记录

---

## 四、错题本

### #1 · bound method 粘的是对象还是名字？
- **时间**：2026-11-02 09:27
- **题目**：预测输出
  ```python
  s = "hello"
  up = s.upper
  s = "world"
  print(up())
  ```
- **我的答案**：`WORLD`（理由：「赋值类似浅拷贝」）
- **正确答案**：`HELLO`
- **为什么错**：
  - 赋值**不是任何形式的拷贝**，它只是把名字标签挂到一个对象上（或者从一个对象挪到另一个对象上）。
  - `s.upper` 先把 `s` 解析成对象 `"hello"`，再把**这个对象**粘进 `up.__self__`。之后 `s = "world"` 只是挪动了标签 `s`。
  ```
  s ──▶ "world"
        "hello" ◀── up.__self__   （这根箭头没动）
  ```
- **知识点**：赋值 = 移动名字标签；bound method 的 `__self__`；对象从来不记得变量名。
- **对比**：赋值（不拷贝）／浅拷贝 `copy.copy`、`[:]`（新外壳，内部共享）／深拷贝 `copy.deepcopy`（一路新建到底）。

### #2 · 赋值 + bound method + 可变列表（#1 的变式）
- **时间**：2026-11-02 09:27
- **题目**：预测输出
  ```python
  a = [1]
  f = a.append
  b = a
  a = [0]
  f(2)
  print(a, b)
  ```
- **我的答案**：第一次 `[1,2],[0,2]`；第二次 `[0,2],[0,2]`
- **正确答案**：`[0] [1, 2]`
- **为什么错**：把 `b = a` 理解成「`b` 跟着名字 `a` 走」，又以为 `f` 会 append 到 `a` *现在*指向的那个列表。实际上标签永远指向**对象**，不会指向另一个名字。
- **正确的逐行推演**：
  ```
  a = [1]        a ─▶ L1=[1]
  f = a.append   f.__self__ ─▶ L1
  b = a          b ─▶ L1
  a = [0]        a ─▶ L2=[0]          （只有 a 动了）
  f(2)           list.append(L1, 2) → L1=[1, 2]
  ```
- **规则**：`x = y` 的意思是「查出 `y` *现在*指向哪个对象，把 `x` 挂上去」。挂完之后 `x` 和 `y` 就是两个独立的标签。

  | 代码 | 发生了什么 | 其他标签看得到变化吗？ |
  |---|---|---|
  | `a = [0]` | 挪动标签 `a` | 看不到 |
  | `a.append(0)` | 修改对象本身 | 看得到，所有指向它的标签都看得到 |
- **知识点**：名字绑定；可变 vs 重新绑定；bound method 的 `__self__`。
- **回炉**：在费曼模式里优先抽这道题。

### #3 · `[[0]*3]*3`：外层的 `* 3` 复制的是引用
- **时间**：2026-11-02 10:02
- **题目**：预测输出
  ```python
  answer = [[0] * 3] * 3
  answer[0][0] = 99
  print(answer)
  ```
- **我的答案**：`[[99,0,0],[0,0,0],[0,0,0]]`（第一次看箭头提示时没看懂，换成「信封 / 房子」的类比后才答对）
- **正确答案**：`[[99, 0, 0], [99, 0, 0], [99, 0, 0]]`
- **为什么错**：以为外层的 `* 3` 会造出三个独立的内层列表。实际上 `[0] * 3` 只造了**一个**列表 `L`，`[L] * 3` 只是把同一个引用放进三个格子：
  ```
  answer[0] ──┐
  answer[1] ──┼──▶ L [0,0,0]
  answer[2] ──┘
  ```
  手写展开后是一样的：`x = [0,0,0]; outer = [x, x, x]`。类比：三个信封上写了同一个地址，但只有一栋房子。
- **验证**：`answer[0] is answer[1]` → `True`
- **正确写法**：`answer = [[0] * n for _ in range(m)]`，因为列表推导式每一轮都会**重新执行** `[0] * n`，所以每一行都是新列表。
- **为什么内层的 `[0] * n` 没问题**：`0` 是 int，int 不能原地修改；只有被重复的元素是可变对象（比如 list）时才会掉坑。
- **知识点**：`list * n` 复制的是引用；名字绑定（和 #1、#2 同一个根源）
- **出处**：LeetCode 1314（见问答记录 Q2）
- **⚠️ 又犯了 2 次**（2026-11-02 10:36、10:52）：1314 的第一版写成 `[[0]*m]*n`（还把 `m`、`n` 写反了）；第二版写成 `[[0]*n]*m`（形状对了，坑还在）。第二次我没看出问题，问「有什么问题吗？」
- **在真实代码里会出什么事**（示例 1，每处理完一行打印一次 `answer`）：
  ```
  after i = 0 : [[12, 21, 16], [12, 21, 16], [12, 21, 16]]
  after i = 1 : [[27, 45, 33], [27, 45, 33], [27, 45, 33]]
  after i = 2 : [[24, 39, 28], [24, 39, 28], [24, 39, 28]]   ← 返回值：最后一行重复 3 遍
  期望结果       [[12, 21, 16], [27, 45, 33], [24, 39, 28]]
  ```
  三个格子指向的是**同一行**，所以外层循环每处理一行都在覆盖上一行写的值，最后只剩最后一行的结果。**不会报错，只是答案悄悄错了。**
- **识别信号**：二维结果里每一行都一样，而且都等于「最后一行该有的值」→ 先怀疑是不是用 `* m` 建的行。
- **习惯**：建二维列表时**一律**写 `[[0] * n for _ in range(m)]`，不用去想内层元素是不是可变的。

### #4 · 夹边界时的 off-by-one
- **时间**：2026-11-02 10:02
- **题目**：补全 `r_start = max(___, i - k)`、`r_end = min(___, i + k)`
- **我的答案**：`0`、`m`
- **正确答案**：`0`、`m - 1`（`r_end` 表示要**包含**的最后一行，循环写 `range(r_start, r_end + 1)`）
- **为什么错**：`m` 是行数，但最后一行的下标是 `m - 1`。用 `m = 3, k = 1, i = 2` 检验：`min(3, 3) = 3` → 第 3 行不存在。
- **两种一致的写法**：
  | `r_end` 的含义 | 表达式 | 循环 |
  |---|---|---|
  | 要包含的最后一行 | `min(m - 1, i + k)` | `range(r_start, r_end + 1)` |
  | 停止的那一行（`range` 的开区间终点） | `min(m, i + k + 1)` | `range(r_start, r_end)` |
- **知识点**：`range` 不包含终点；下标 vs 长度；选定一种区间写法就一直用它
- **出处**：LeetCode 1314（见问答记录 Q2）

### #5 · `except` 的顺序：只有第一个匹配的分支会执行
- **时间**：2026-11-02 10:36
- **题目**：预测输出
  ```python
  try:
      raise CustomError("oops")      # CustomError 继承自 Exception
  except Exception:
      print("A")
  except CustomError:
      print("B")
  ```
- **我的答案**：`B`（经过提示后改成 `A`）
- **正确答案**：`A`，并且只打印 `A`
- **为什么错**：以为 Python 会找「最精确」的那个 `except`。实际上它是**从上到下**用 `isinstance` 检查，第一个匹配的分支执行完就跳出整个 `try` 语句。`CustomError` 是一种 `Exception` → 第一个分支就匹配上了 → `except CustomError` 成了永远执行不到的死代码。
- **正确写法**：先写具体的，后写宽泛的
  ```python
  except CustomError:   print("B")
  except Exception:     print("A")   # 兜底
  ```
  类比：分拣信件时先看「给 Alice 的信」，再看「所有信件」。
- **知识点**：异常匹配 = `isinstance`；继承里「是一种」的关系；`except` 的顺序
- **出处**：问答记录 Q3

### #6 · 类里的辅助方法：调用时没加 `self.`，定义时也漏了 `self`
- **时间**：2026-11-02 10:36
- **题目**：（自己写的 1314 代码）在 `matrixBlockSum` 里调用辅助方法
- **我的写法**：`answer[i][j] = __Sum__(mat, k, i, j)`，定义是 `def __Sum__(mat, k, r, c):`
- **报错**：`NameError: name '__Sum__' is not defined. Did you mean: 'self.__Sum__'?`
- **正确写法**：
  ```python
  def _block_sum(self, mat, k, r, c): ...
  answer[i][j] = self._block_sum(mat, k, i, j)
  ```
- **为什么错**：
  1. 方法是类的属性，不是方法体里能直接用的名字 → 必须通过 `self.`（或 `Solution.`）去拿。
  2. `self._block_sum(mat, k, i, j)` 是 bound method 调用 → `Solution._block_sum(self, mat, k, i, j)`，所以定义里第一个参数必须是 `self`，否则会得到 `TypeError: takes 4 positional arguments but 5 were given`。
- **另外**：同一份代码里，第 13 行又写了 `[[0]*m]*n` → 刚记完错题本 #3 就又犯了，而且 `m`、`n` 写反了。复习重点：**写代码时要主动用上学过的规则。**
- **知识点**：`self`、bound method（Q1）；命名规范（Q4）
- **出处**：问答记录 Q4

### #7 · 方法里写 `count = count + 1`：以为改的是类变量
- **时间**：2026-11-02 13:37
- **题目**：预测 `Counter()` 运行时会发生什么
  ```python
  class Counter:
      count = 0
      def __init__(self):
          count = count + 1
  c = Counter()
  ```
- **我的答案**：`1`（以为 `Counter.count` 会变成 1）；经过提示后答「undefined」，方向对了
- **正确答案**：报错 `UnboundLocalError: cannot access local variable 'count' where it is not associated with a value`
- **为什么错**：
  1. 方法里不带前缀的 `count` 是**局部变量**，和类变量 `count = 0` 只是同名而已。
  2. Python 执行前先扫方法体，看到 `count = ...`，就认定 `count` 在整个方法里都是局部变量。
  3. 算右边 `count + 1` 时要读这个局部 `count`，但它还没被赋值 → 报错。
- **正确写法**：`Counter.count += 1`
- **变式（答对 ✅）**：写成 `self.count += 1` → 结果 `Counter.count` 仍然是 0。读的时候从类上拿到 0，写的时候在对象身上新建了一个实例变量，把类变量遮住了。
- **知识点**：局部 / 实例 / 类三种变量；Python 在执行前就确定了哪些名字是局部变量；遮蔽
- **出处**：问答记录 Q6

### #8 · 用了 `++`（Python 里没有这个运算符）
- **时间**：2026-11-02 13:37
- **题目**：写一行代码，让类变量 `Counter.count` 加 1
- **我的答案**：`Counter.count++`
- **正确答案**：`Counter.count += 1`（或 `Counter.count = Counter.count + 1`）
- **为什么错**：`++` 是 C / Java / JavaScript 的写法，Python 没有这个运算符。
  - `x++` → `SyntaxError`
  - `++x` → **不报错，但什么都不做**：会被理解成 `+(+x)`，值不变，也不会写回去 ← 更隐蔽的坑
- **前缀是对的**：`Counter.count` 正确地指向了类变量 ✅
- **知识点**：Python 的自增写法；不要把别的语言的语法搬过来
- **出处**：问答记录 Q6

### #9 · 函数最后忘了 `return` → 返回 `None`
- **时间**：2026-11-02 14:24
- **题目**：（自己写的 1314 前缀和版本）`matrixBlockSum` 把 `answer` 填满之后就结束了
- **现象**：示例 1 的输出是 `None`，没有报错
- **为什么错**：函数执行到最后都没碰到 `return` 语句，Python 就自动返回 `None`。
- **正确写法**：在函数末尾加 `return answer`
- **识别信号**：结果是 `None`，或者报 `'NoneType' object is not subscriptable / iterable` → 先检查有没有 `return`。
- **知识点**：函数的返回值；隐式 `return None`
- **出处**：问答记录 Q7

### #10 · 坐标约定前后不一致：x = 列，却写了 `preSum[x][y]`
- **时间**：2026-11-02 14:24
- **题目**：（自己写的 1314 前缀和版本）
  ```python
  # matrixBlockSum 里
  x1 = max(0, j-k); y1 = max(0, i-k)    # x ← j（列）
  # sumRegion 里
  return preSum[x2+1][y2+1] - ...        # x 放在了第一个下标的位置（行）
  ```
- **现象**：示例 1 返回 `[[12,27,24],[21,45,39],[16,33,28]]`，是期望答案 `[[12,21,16],[27,45,33],[24,39,28]]` 的**转置**；用 2×3 矩阵会报 `IndexError`。
- **我的想法**：「我两边都想让 x 表示横坐标」→ 想法是一致的，**写法**不一致。
- **为什么错**：`list[a][b]` 的第一个下标选的是**行**（纵向），所以 `preSum[x][y]` 实际上把 x 当成了纵坐标，和数学里写 `(x, y)` 的顺序正好相反。
- **另一个弯路**：把 `x ← i`、`y ← j` 对调后，结果对了，但 x 就不再是横坐标了 → 代码对了，名字却在骗人。
- **正确写法（任选一种，全程只用这一套）**：
  - x = 列：`p[y2+1][x2+1] - p[y1][x2+1] - p[y2+1][x1] + p[y1][x1]`
  - x = 行（题解的做法）：`x ← i`，`preSum[x][y]`
  - `row1, col1, row2, col2`：没有歧义（推荐）
- **为什么 3×3 的例子会「骗人」**：正方形矩阵把行列弄反不会越界，只是结果被转置了 → **测试时要用非正方形矩阵**。
- **知识点**：二维列表的下标是 `[行][列]` = `[y][x]`；bug 往往出现在两套约定交接的地方；名字是写给人看的
- **出处**：问答记录 Q7

### #11 · 3Sum：`elif` 条件写成和 `if` 一样 + `else` 里指针不动 → 超出内存限制
- **时间**：2026-11-07 11:54
- **题目**：（自己写的 LeetCode 15 `twoSumTarget`）
  ```python
  if sum < target:
      ...
  elif sum < target:          # 和上面一模一样
      ...
  else:
      res.append([left, right])   # 记的是下标
      while left < right and nums[left] == nums[left+1]: left += 1
      while left < right and nums[right] == nums[right-1]: right -= 1
      # 没有 left += 1 / right -= 1
  ```
- **现象**：`[-1,0,1,2,-1,-4]` 超出内存限制
- **为什么错**：`sum > target` 时两个条件都不满足，掉进 `else`；没有重复元素时两个 `while` 一次都不执行，`left`、`right` 原地不动 → 死循环，同一组结果被无限 `append` → 内存爆掉。
- **顺带的问题**：`append([left, right])` 加的是下标，应是 `[nums[left], nums[right]]`；外层 `while i < n and nums[i] == nums[i+1]` 在 `i = n-1` 时越界，应写 `i < n-1`。
- **识别信号**：「超出内存限制 / 超时」→ 先找**出不去的循环**：每个分支走完后，循环变量一定变了吗？复制粘贴的条件要逐个核对。
- **知识点**：`if/elif` 条件互斥；循环必须有进展；双指针
- **出处**：问答记录 Q11

### #12 · 3Sum：`left += 1; right -= 1` 写在 `if/elif/else` 外面 → 漏答案
- **时间**：2026-11-07 11:54
- **题目**：第二版 `twoSumTarget`，每个分支已经用 `while nums[left] == low` 跳到新值了，循环末尾又写了：
  ```python
          left += 1
          right -= 1
  ```
- **现象**：`[-1,0,1,2,-1,-4]` → `[[-1,2,-1]]`（漏了 `[-1,0,1]`）；`[-2,0,1,1,2]` → 漏了 `[-2,1,1]`
- **为什么错**：写在分支外面 = **每个分支**都多走一步。① `else` 里的 `while nums[left] == low` 至少执行一次，已经停在新值上，再 `+1` 就跳过了一个元素；② `sum < target` 时只该动 `left`，`right -= 1` 把可能配对的 `right` 也扔掉了。
  跟踪 `i = 1`：`(2,5)` 记录 `[-1,2]` → 两个 `while` 后 `(3,4)`，正好 `0 + 1 = 1` 是答案 → 末尾两行变成 `(4,3)`，错过。
- **正确写法**：删掉这两行。每个指针的移动写在**自己的分支里**。
- **知识点**：代码放在分支里面还是外面；`while` 停下时指针指在哪里
- **出处**：问答记录 Q11

### #13 · 3Sum：「先走一步，再跳重复」→ 把可配对的元素跳过了
- **时间**：2026-11-07 11:54
- **题目**：
  ```python
  if sum < target:
      left += 1
      while left < right and nums[left] == nums[left+1]:
          left += 1
  ```
- **我的想法**：想在 `if/elif` 分支里也跳过重复值，提高效率。
- **现象**：`[-2,0,1,1]` 返回 `[]`，应该是 `[[-2,1,1]]`
- **为什么错**：`nums[left] == nums[left+1]` 这种 `while` 会停在**重复串的最后一个**。先 `+1` 已经落到新值（第一个 1）上，再跳就把新值的重复串也跳过了：`left` 被推到 `right` 的位置，错过了 `1 + 1 = 2`。
- **正确写法**（任选一种）：
  - `if/elif` 只走一步，只在 `else` 里去重（最简单）
  - 调换顺序：先 `while nums[left] == nums[left+1]: left += 1`，再 `left += 1`
  - 先存 `low = nums[left]`，再 `while nums[left] == low: left += 1`（推荐，三个分支同一套模式）
- **知识点**：两种跳重复写法停的位置差一格；跳完之后指针要停在新值上
- **出处**：问答记录 Q11

### #14 · `a, *b, c = [1, 2]`：`*b` 拿到的是什么？
- **时间**：2026-11-03 03:59
- **题目**：预测输出 `a, *b, c = [1, 2]; print(a, b, c)`
- **我的答案**：`1, 0, 2` → 提示后改成 `None`
- **正确答案**：`1 [] 2`
- **为什么错**：`*b` 的工作是「把剩下的元素装进一个列表」，**永远**造一个列表。剩 2 个 → `[2, 3]`；剩 1 个 → `[2]`（还是列表）；剩 0 个 → `[]`；不够分 → `ValueError`。`0`（整数）、`None`（什么都没有）、`[]`（存在但为空的列表）是三种不同的东西。
- **知识点**：解包；`0` / `None` / `[]` 的区别
- **出处**：问答记录 Q14

### #15 · 724：属性找错了对象、局部变量跨方法用、前缀和下标没换算
- **时间**：2026-11-02 09:00
- **题目**：（自己写的 724，代码见 Q12）
- **现象**：`AttributeError: 'Solution' object has no attribute 'preSum'`；修好后还有 3 个隐藏 bug
- **为什么错**：
  1. `self.preSum` 写在 `Solution` 的方法里，`self` 是 `Solution` 对象，而 `preSum` 挂在 `Sum` 对象上 → `sum.preSum`（或者让 `findIndex` 自己用 `self.preSum`）
  2. `n` 是 `__init__` 的局部变量，`findIndex` 里看不到 → `NameError`
  3. `preSum` 长度 `n+1`，`preSum[n+1]` 越界，总和是 `preSum[n]`
  4. `i` 是 `preSum` 的下标，返回 `nums` 的下标要 `i - 1`
- **识别信号**：`'X' object has no attribute 'y'` → 先问「这里的 `self` 是谁？`y` 是挂在谁身上的？」
- **知识点**：`self` 是调用方法的那个对象；局部变量的作用域；前缀和数组比原数组多一位
- **出处**：问答记录 Q12

### #16 · 370：方法没加 `()`、没加 `self.`，类型注解写成圆括号
- **时间**：2026-11-03 03:53
- **题目**：
  ```python
  difference.multiIncrement          # 没调用
  return difference.result           # 返回的是方法对象，不是结果
  ...
  increment(self.diff, i[0], i[1], i[2])     # 没加 self.，还多传了 self.diff
  def multiIncrement(self, operations: list(list[int])):   # 注解用了圆括号
  ```
- **为什么错**：不加 `()` 只是拿到 bound method 对象，方法根本没执行；`multiIncrement` 还需要传 `operations`。在方法里调用同类的方法要 `self.increment(...)`，`self` 自动传入，`self.diff` 方法内自己能拿到（错题本 #6 又出现了）。注解应写 `list[list[int]]`。
- **正确写法**：
  ```python
  difference.multiIncrement(operations)
  return difference.result()
  for start, end, val in operations:
      self.increment(start, end, val)
  ```
- **识别信号**：结果是 `<bound method ...>`，或者函数里的代码像是「没跑」→ 检查有没有 `()`。
- **知识点**：bound method 对象 vs 调用；`self.` 前缀；类型注解用方括号
- **出处**：问答记录 Q13

### #17 · 151：分隔符写错；以为 `split(" ")` 会留下 `' '`
- **时间**：2026-11-03 05:01
- **题目**：（151 截图）`str_list = s.split(',')`；`cleanSpaces` 里判断 `if obj == ' '`
- **为什么错**：① 单词是用空格分隔的，没有逗号 → `split(',')` 整个字符串变成一块。② `split(" ")` 每遇到一个空格切一刀，多余的空格变成 `''`（空字符串），不是 `' '`，所以 `== ' '` 永远匹配不到。
- **正确写法**：`s.split()`（不传参数）：任意空白分隔、连续空白算一个、首尾空白丢掉，结果里没有 `''`。
- **知识点**：`split()` vs `split(" ")`
- **出处**：问答记录 Q15

### #18 · 151：方法的主语搞错——`pop(x)`、`list.join`
- **时间**：2026-11-03 05:01 / 05:21
- **题目**：
  ```python
  pop(str_list[index])                 # 删除
  self.reversed_str_list.join(" ")     # AttributeError: 'list' object has no attribute 'join'
  ```
- **为什么错**：① `pop` 是列表的方法，要写 `str_list.pop(...)`；而且参数是**下标**，传的却是元素（删元素用 `remove`）。另外这是在边遍历边删除，会跳过元素。② `join` 是**字符串**的方法：`" ".join(列表)`，粘合剂是主语。
- **正确写法**：`" ".join(words)`；删除用推导式 `[v for v in a if v != '']`
- **识别信号**：`'list' object has no attribute ...` / `NameError: name 'pop' ...` → 想一想「这个方法属于哪种类型？」
- **知识点**：方法属于某种类型的对象；`pop(下标)` vs `remove(值)`；不要边遍历边删除
- **出处**：问答记录 Q15

### #19 · 151：切片 `[-1:0:-1]` 漏了下标 0；`[''] * n` 占位留下空位
- **时间**：2026-11-03 05:21
- **题目**：
  ```python
  self.reversed_str_list = [''] * len(self.str_list)
  for word in self.str_list[-1:0:-1]:
      self.reversed_str_list[index] = word; index += 1
  ```
- **为什么错**：切片的结束下标不包含 → `[-1:0:-1]` 到下标 1 就停了，漏掉第一个单词；4 个位置只填了 3 个，剩一个 `''`，`join` 后末尾多一个空格。
- **正确写法**：`words[::-1]`（开始结束都省略 = 全部）；不需要预先占位，用 `[]` + `append`，或者直接 `" ".join(s.split()[::-1])`。
- **知识点**：切片 / `range` 结束不包含（错题本 #4）；倒序要到 0 得写 `range(n-1, -1, -1)` 或 `[::-1]`
- **出处**：问答记录 Q15

### #20 · 54 螺旋矩阵：`if` 条件方向反了、`<` 应为 `<=` → 死循环超时
- **时间**：2026-11-03 07:27
- **题目**：（54 截图）每个方向前面判断「还有没有格子」，上边写的是 `if lower_bound < upper_bound:`，左右写的是 `if left_bound < right_bound:` 这类严格小于
- **现象**：超出时间限制；`output` 停在 `[3, 6, 9, 7, 4, 1]`
- **为什么错**：`2 < 0` 为 False，第一行整个被跳过；只剩一列时 `1 < 1` 为 False，这一列也被跳过 → `output` 不再增长，`while len(output) < m*n` 永远成立。
- **正确写法**：上/下边 `if upper <= lower:`；右/左边 `if left <= right:`
- **识别信号**：超时但数据不大 → 死循环；先把每个条件翻译成一句人话（「这条边上还有格子吗」）再写
- **知识点**：边界相等的情况；比较方向
- **出处**：问答记录 Q16

### #21 · 76：`start = right`；移出字符时无条件 `valid -= 1`
- **时间**：2026-11-05 15:42
- **题目**：（代码见 Q20）
- **现象**：`"ADOBECODEBANC"/"ABC"` → `"ADOBEC"`（应为 `"BANC"`）；`"AAB"/"AB"` → `"AAB"`（应为 `"AB"`）
- **为什么错**：① 窗口是 `[left, right)`，起点是 `left`。② `valid` 记的是「数量已经够了的字符种数」，移出一个字符后可能还够（`"AB"` 里 A 还有 1 个），这时不能减 → 提前停止收缩。
- **正确写法**：
  ```python
  if d in need:
      if window[d] == need[d]:
          valid -= 1
      window[d] -= 1
  ```
- **知识点**：计数器只在「刚好跨过界限」时变化，加入和移出对称；判断放在 `-= 1` 前面
- **出处**：问答记录 Q20

### #22 · 567：窗口大小用了 `len(need)`，应是 `len(s1)`
- **时间**：2026-11-06 03:27
- **题目**：`if right - left == len(need):`
- **现象**：87 个用例通过，`s1 = "abcdxabcde"`、`s2 = "abcdeabcdx"` 输出 `false`（应为 `true`）
- **为什么错**：`len(need)` 是不同字符的**种数**（5），`len(s1)` 是字符**个数**（10）。s1 没有重复字符时两者相等，所以大部分用例碰巧通过。
- **正确写法**：窗口大小用 `len(s1)`；`valid == len(need)` 那一行保持不变。
- **识别信号**：大部分用例过、个别失败 → 找「什么输入下两个量恰好相等」；测试时加有重复字符的用例
- **知识点**：字典的长度 = key 的个数
- **出处**：问答记录 Q21

### #23 · 在 `for` 循环体里改循环变量 `i`，以为能跳过元素
- **时间**：2026-11-07 12:00
- **题目**：3Sum 外层用 `for i in range(len(nums)):`，循环体末尾 `while nums[i] == nums[i+1]: i += 1`
- **现象**：答案错误，出现重复的三元组
- **为什么错**：每轮开始 `for` 都会把 `range` 的下一个值重新赋给 `i`，循环体里改 `i` 只影响这一轮剩下的代码。
- **正确写法**：用 `while` 自己控制 `i`；或者 `for` + `if i > start and nums[i] == nums[i-1]: continue`
- **知识点**：`for` 循环变量每轮被重新赋值；名字标签
- **出处**：问答记录 Q22

### #24 · 4Sum：被复用的 `threeSumTarget` 里 `i = 0`，没用参数 `start`
- **时间**：2026-11-07 12:10
- **题目**：`def threeSumTarget(self, nums, start, target): ... i = 0`
- **现象**：输出 12 组，有 `[0, 2, -1, -1]`（`-1` 只有一个却用了两次），同一组换顺序重复出现
- **为什么错**：每次都从下标 0 开始找，外层已经用过的元素被重复使用。3Sum 里外层传的 `start` 正好是 0，bug 被掩盖了。
- **正确写法**：`i = start`
- **识别信号**：参数在函数体里一次都没用到 → 多半是 bug（编辑器常会把它标灰）
- **知识点**：函数参数；「碰巧对」的代码
- **出处**：问答记录 Q23

### #25 · 4Sum：先跳重复，再处理 → `[2,2,2,2,2]` 返回 `[]`
- **时间**：2026-11-07 12:10
- **题目**：
  ```python
  while i < n:
      while i < n-1 and nums[i] == nums[i+1]: i += 1   # 先跳
      triples = self.threeSumTarget(nums, i+1, target-nums[i])
  ```
- **为什么错**：先跳到重复串的**最后一个**再处理，后面相同的值就用不上了（`i` 直接到 4，后面没有元素）。和 #13 同一个道理。
- **正确写法**：先处理当前元素，再跳重复；或者 `if i > start and nums[i] == nums[i-1]: continue`（和前一个比，跳过的是**后面**的重复）
- **另**：`target: long` → Python 没有 `long`，写 `int`
- **知识点**：去重的时机
- **出处**：问答记录 Q23

### #26 · nSum 递归版：整个程序没有 `nums.sort()`
- **时间**：2026-11-07 12:30
- **现象**：`[1,0,-1,0,-2,2]`、`target = 0` → `[[-2, 2, 0, 0]]`（应有 3 组）
- **为什么错**：双指针（`sum < target` 就 `left` 右移）和「与前一个比较去重」都依赖数组有序；重构成递归时把 `sort()` 弄丢了。
- **正确写法**：在 `fourSum` 里 `nums.sort()` 一次，不要放在递归函数里
- **识别信号**：重构后结果变少/变乱 → 对比重构前少了哪一行
- **知识点**：双指针的前提是有序；递归函数里避免重复做只需做一次的事
- **出处**：问答记录 Q24

### #27 · 42 接雨水：`min(l_max, r_max) - height[i]` 可能是负数
- **时间**：2026-11-07 13:00
- **题目**：`l_max` 用 `range(i)`、`r_max` 用 `range(i+1, n)`，都不包含 `i`
- **现象**：两个示例通过；`[1, 2, 1]` 会算出 -1（应为 0）
- **为什么错**：`i` 比两边都高时，`min(...)` 小于 `height[i]`，加上了负数
- **正确写法**：范围包含 `i` 自己（`range(i+1)`、`range(i, n)`），或者只加正数
- **识别信号**：示例过了不等于对 → 自己构造「中间最高」这类极端小例子
- **知识点**：边界包含与否；构造测试用例
- **出处**：问答记录 Q25

### #28 · 二分左边界：只检查了越界，没检查 `nums[left] == target`
- **时间**：2026-11-07 14:30
- **题目**：（自己的总结）「`left` 只可能上越界，所以只用写 `if left > len(nums)-1`」
- **为什么错**：越界分析对，但 `left` 是「第一个 `≥ target`」，可能 `>`。`[1, 3, 5]` 找 2：`left = 1` 没越界，`nums[1] = 3`，数组里根本没有 2。
- **正确写法**：
  ```python
  if left >= len(nums) or nums[left] != target:
      return -1
  return left
  ```
  顺序不能反（短路保护越界）
- **知识点**：二分的返回值含义；`or` 短路
- **出处**：问答记录 Q26

### #29 · `def f(*args): print(args)`：忘了 `args` 是元组
- **时间**：2026-11-08 10:46
- **题目**：`nums = [1, 2, 3]`，预测 `f(nums)` 和 `f(*nums)` 的输出
- **我的答案**：第一次 `[1,2,3]` + 三行 `1` `2` `3` → 提示后 `[1,2,3]` / `1 2 3`
- **正确答案**：`([1, 2, 3],)` / `(1, 2, 3)`
- **为什么错**：`*args` 不管收到几个参数都装进**元组**。`f(nums)` 只收到 1 个参数（列表）→ 单元素元组 `(x,)`；`f(*nums)` 先解包成 3 个参数再打包。`1 2 3` 是 `print(*args)` 的输出。
- **知识点**：`*args` 打包成元组；单元素元组要有逗号；调用时的 `*` 解包
- **出处**：问答记录 Q28

### #30 · `h(x=1, y=2)` 里 `**kwargs` 的 key 是字符串
- **时间**：2026-11-08 10:46
- **题目**：`def h(**kwargs): print(kwargs)`，`h(x=1, y=2)` 输出什么
- **我的答案**：`{x: 1, y:2}`
- **正确答案**：`{'x': 1, 'y': 2}`
- **为什么错**：`x=1` 里的 `x` 是参数**名字**，存成字符串 key `'x'`；`{x: 1}` 的意思是「用变量 `x` 的值当 key」，没有这个变量会 `NameError`。取值要写 `kwargs['x']`。
- **知识点**：关键字参数；字典的 key；名字 vs 字符串
- **出处**：问答记录 Q28

### #31 · 1011 `f`：装不下的货被外层 `i += 1` 跳过了
- **时间**：2026-11-08 17:36
- **题目**：
  ```python
  while i < len(weights):
      x = capacity
      while x - weights[i] >= 0 and i < len(weights) - 1:
          x -= weights[i]; i += 1
      days += 1
      i += 1          # 无条件
  ```
- **现象**：`capacity = 10` 算出 4 天，`15` 算出 3 天（都偏少）；最终答案 7（应为 15）
- **为什么错**：内层因为「装不下」停下时，`i` 指着还没装的货；外层无条件 `i += 1` 把它跳过了。`i < len - 1` 让最后一件货靠外层 `i += 1` 假装装上。
- **正确写法**：装上才 `i += 1`，装不下 `break`、`i` 不动（代码见 Q30）
- **识别信号**：结果偏少 / 偏小 → 有元素被漏掉；检查每个 `i += 1` 前，元素是否真的处理完了
- **知识点**：先检查、再更新；指针的含义（下一个待处理的元素）
- **出处**：问答记录 Q30

### #32 · 1011：二分的上下界写成 `1, 500`
- **时间**：2026-11-08 17:36
- **题目**：`left, right = 1, 500`（求 `max` 和总和的两行被注释掉）
- **为什么错**：`left` 必须 ≥ 最重的货，否则那件货永远装不上（旧 `f` 假装运走，新 `f` 会死循环）；`right` 至少是总重量（`days = 1` 时一天运完），500 只是单件货的上限。
- **正确写法**：`left = max(weights)`，`right = sum(weights)`
- **知识点**：二分答案的搜索范围要从题意推：最小可能的答案 ~ 一定够用的答案
- **出处**：问答记录 Q30

### #33 · 239 单调队列：检查 `q[-1]`，删除却用 `popleft()`
- **时间**：2026-11-08 17:36
- **题目**：`if self.max_queue[-1] == number: self.max_queue.popleft()`
- **我的想法**：先以为是 push / pop 顺序的问题；又以为 `[-1]` 和 `popleft` 「都是队尾」。
- **现象**：示例通过，提交错误；`[0, 5, 3, 2, 5], k = 2` → `[5, 5, 5, 5]`（应为 `[5, 5, 3, 5]`）
- **为什么错**：`q[-1]` 是右边（队尾，最新），`popleft()` 删左边（队头，最老）。要滑出的是最老的元素，在左边，但检查看的是右边 → 条件不成立，该走的最大值留在队里。
- **正确写法**：`if self.max_queue[0] == number: self.max_queue.popleft()`
- **知识点**：deque 的两头：`[0]` / `popleft` / `appendleft` = 左；`[-1]` / `pop` / `append` = 右
- **出处**：问答记录 Q32

### #34 · 141 环形链表：`while fast.next is not None` → `fast` 自己是 None 时崩溃
- **时间**：2026-11-08 19:46
- **题目**：快慢指针判断有没有环，`fast` 每次走两步
- **我的写法**：`while fast.next is not None:`
- **现象**：`head = [1, 2]` → `AttributeError: 'NoneType' object has no attribute 'next'`；有环或奇数长度的用例都能过
- **为什么错**：偶数长度时 `fast = fast.next.next` 直接跳到 None，再查 `None.next` 就崩。只检查了第二层，没检查第一层。
- **正确写法**：`while fast and fast.next:`（顺序不能反，靠 `and` 短路）
- **知识点**：访问 `x.next.next` 前，`x` 和 `x.next` 都要确认不是 None——访问几层，检查几层；另外 141 的返回注解应为 `-> bool`
- **出处**：问答记录 Q37

### #35 · 23 合并 K 个链表：没跳过空链表 + `heappop` 漏了 `heapq.`
- **时间**：2026-11-09 14:28
- **题目**：
  ```python
  for i, head in enumerate(lists):
      heapq.heappush(pq, (head.val, i, head))
  ...
  val, i, head = heappop(pq)
  ```
- **现象**：`lists = [[]]` → `AttributeError: 'NoneType' object has no attribute 'val'`；修好后还会 `NameError: name 'heappop' is not defined`
- **为什么错**：① `if not lists` 只挡住了外层空列表，挡不住「里面的链表是空的」（`head` 是 None）；② `import heapq` 之后函数要写 `heapq.heappop`。
- **正确写法**：push 前加 `if head is not None:`；`val, i, head = heapq.heappop(pq)`
- **知识点**：容器空不空 ≠ 元素空不空；名字要说清楚是谁的（模块前缀，和漏 `self.` 同类，见 #6）
- **出处**：问答记录 Q39

### #36 · 以为 `not head` 和 `head is not None` 是一回事
- **时间**：2026-11-09 14:30
- **题目**：23 题 push 前要加什么判断？
- **我的想法**：「`not head` 和 `head is not None` 不是一回事吗？」
- **为什么错**：两者正好相反。`not head` ⇔ `head is None`；`head`（直接写）⇔ `head is not None`。
- **另一个区别**：`if x:` 看真值，`0`、`""`、`[]` 也算假；`is not None` 只排除 None → 下标 0、空列表这类值要用 `is None` 判断
- **知识点**：真值 vs 和 None 比较
- **出处**：问答记录 Q40

### #37 · 160 相交链表：把「会死循环的写法」判断反了
- **时间**：2026-11-09 15:32
- **题目**：`p1 = headB if p1 is None else p1.next`（下）vs `p1 = p1.next if p1.next is not None else headB`（上）
- **我的想法**：下面那种遇到不相交的链表会一直空转
- **为什么错**：正好相反。下面那种会让指针真的走到 None，两人路程相等（lenA + 1 + lenB），不相交时会**同时**到达 None → 退出。上面那种跳过了 None，在节点之间一直转，永远不相等 → 死循环。
- **知识点**：None 是不相交时的「虚拟交点」；判断死循环要代入具体例子跟踪（`A = 1→2, B = 3`）
- **出处**：问答记录 Q41

### #38 · 把 O(log N) 当成能直接算出高度的公式
- **时间**：2026-11-10 18:32
- **题目**：4 个节点（1、2、3、4）的高度平衡树，高度是 3，log₂4 = 2，为什么对不上？
- **为什么错**：O(·) 只说「≤ 常数 × log N」，藏了常数和 ±1；高度按节点数还是按边数数也差 1。平衡树最坏高度约 1.44 log₂N，4 个节点高 3 正好是最坏情况（最少节点数 1, 2, 4, 7, …）。
- **知识点**：复杂度描述增长速度，不是等式
- **出处**：问答记录 Q43

### #39 · 94 中序遍历：嵌套函数定义时写了 `self`；类型注解又写成了圆括号
- **时间**：2026-11-10 19:45
- **题目**：
  ```python
  def inorderTraversal(self, root):
      def traversal(self, root: Optional(TreeNode)):
          ...
      traversal(root)
  ```
- **现象**：`TypeError: Solution.inorderTraversal.<locals>.traversal() missing 1 required positional argument: 'root'`
- **为什么错**：嵌套函数是普通函数，不是方法，调用时不会自动传 self → `root` 被塞进 `self`，`root` 缺了。`<locals>` 就是在提示它是局部函数。
- **正确写法**：`def traversal(root):`（或者写成类的方法，用 `self.traversal(...)` 调用）；注解写 `Optional[TreeNode]`
- **知识点**：只有直接写在 class 里的方法才有 self；注解用方括号（**和 #16 同一个错，第 2 次**）
- **出处**：问答记录 Q44

### #40 · 145 后序遍历：把 `res = []` 写成类变量，方法里直接用 `res`
- **时间**：2026-11-10 19:59
- **题目**：
  ```python
  class Solution:
      res = []
      def postorderTraversal(self, root):
          ...
          res.append(root.val)
  ```
- **现象**：`NameError: name 'res' is not defined. Did you mean: 'self.res'?`
- **为什么错**：① LEGB 不包括类体，方法里看不到类变量的裸名字；② 就算改成 `self.res`，类变量列表被所有 Solution 实例共用，多个用例的结果会累积到一起。
- **正确写法**：嵌套函数 + 外层局部 `res`；或入口方法里 `self.res = []` + 另一个递归方法；或用返回值拼接
- **知识点**：类变量 vs 实例变量；方法里访问类变量必须 `self.` / `类名.`（和 #7 同一类）
- **出处**：问答记录 Q46

### #41 · 102 层序遍历：`cur = dq[0]` 写在 for 外面，以为它会「动态锁定」队头
- **时间**：2026-11-10 20:26
- **题目**：每层开始时 `cur = dq[0]`，for 里用 `cur.left` 判断、`dq[0].left` 入队、`dq.popleft()` 出队
- **现象**：`[3,9,20,null,null,15,7]` → `[[3],[9,20]]`，少了 `[15,7]`
- **我的想法**：「cur 不是动态锁定这个队列的头？」
- **为什么错**：赋值绑定的是**那一刻的对象**，不是 `dq[0]` 这个表达式。第 2 层里 `cur` 一直是 9，20 出队时检查的还是 9 的孩子 → 15、7 没进队。
- **正确写法**：for 里第一行 `cur = dq.popleft()`，之后统一用 `cur`
- **知识点**：变量 = 贴在对象上的标签（和 #1–#3 同一个根源）；同一个节点不要混用两种写法
- **出处**：问答记录 Q47

### #42 · 111 最小深度：`self.depth += 1` 之后，有两个出口没有 `-= 1`
- **时间**：2026-11-11 11:47
- **题目**：叶子节点 `return`、剪枝 `return` 都在 `self.depth -= 1` 之前
- **现象**：期望 2，输出 3（本地跑是 4）；打印发现节点 5（根的孩子）的 depth 是 4
- **为什么错**：进入 +1、离开 −1 必须成对；漏掉的出口让 depth 越来越大，兄弟节点、后面的分支深度全算错。
- **正确写法**：每个出口返回前都 `self.depth -= 1`；更好的是把 depth 当参数传：`traverse(node, depth + 1)`，不用手动撤销
- **知识点**：共享状态的「做了要撤销」（回溯同理）；参数传递 vs 共享变量
- **出处**：问答记录 Q48

### #43 · 543 直径：递归调了入口函数而不是辅助函数；初始值 `-inf`；注解又写成圆括号
- **时间**：2026-11-11 13:44
- **题目**：`traverse` 里写 `left = self.diameterOfBinaryTree(root.left)`
- **现象**：`[1,2,3,4,5]` 输出 `-inf`（应为 3），空树也是 `-inf`
- **为什么错**：`diameterOfBinaryTree` 返回 `max_diameter`，不是深度；`traverse(None)` 返回的 0 被丢掉，所有深度都成了 `-inf`。空树时 max 从没更新 → `-inf`。
- **正确写法**：`left = self.traverse(root.left)`；`self.max_diameter = 0`；`Optional[TreeNode]`
- **知识点**：入口函数和递归辅助函数各管各的返回值（方法调用写错对象，见 #6、#16、#18）；`Optional(...)` **第 3 次**（#16、#39）
- **出处**：问答记录 Q50

### #44 · partition：以为 j 也会停在 9
- **时间**：2026-11-11 12:23
- **题目**：`[4, 4, 2, 1, 9, 7]`，pivot = 4，第 3 轮 i 从 3、j 从 4 出发
- **我的想法**：i 先动停在 9，j 也停在 9
- **为什么错**：i 和 j 的停止条件相反：i 跳过 ≤pivot、停在 >pivot；j 跳过 >pivot、停在 ≤pivot。9 对 j 来说是要跳过的 → j 走到 3（值 1）才停。结束时两指针交错，`j = i - 1`。
- **知识点**：双指针各自的循环不变量；交换后不回起点
- **出处**：问答记录 Q49

### #45 · 230 第 k 小：把局部排名当成全局排名
- **时间**：2026-11-11 16:01
- **题目**：找 k = 4，走到节点 4 时 `rank = left_size + 1 = 1`
- **我的想法**：「rank 怎么是 1？不是 4 嘛？」
- **为什么错**：rank 只算当前子树里的名次；前面往右走时已经 `k -= 3` 扣掉了左边的名次。全局排名 = 已扣掉的 3 + 局部 1 = 4。
- **知识点**：递归 / 迭代里的量要说清楚「相对于谁」：k 和 rank 都是相对当前子树的
- **出处**：问答记录 Q52

### #46 · 98 验证 BST：参数名 `min` / `max` 遮住内置函数；注解又写成圆括号
- **时间**：2026-11-11 17:41
- **题目**：`def traverse(self, root: Optional(TreeNode), min: Optional(TreeNode), max: Optional(TreeNode)):`
- **为什么错**：① 参数名 `min` / `max` 会遮住内置的 `min()` / `max()`，函数里就用不了它们（后序版里正好要用 `min(l_min, node.val)`）；② `Optional(...)` 应为 `Optional[...]`。
- **正确写法**：`def traverse(self, root: TreeNode | None, lo: TreeNode | None, hi: TreeNode | None):`
- **知识点**：别用内置函数名当变量名（`list`、`dict`、`sum`、`min`、`max`、`id`）；注解用方括号（**第 4 次**，见 #16、#39、#43）
- **出处**：问答记录 Q54

### #47 · 把「x 序」「DFS」和「要不要 return」混为一谈
- **时间**：2026-11-11 17:46（18:09）
- **题目**：98 传 `(lo, hi)` 的版本是前序吗？最后的 `return` 该写在哪？
- **我的想法**：「如果是前序遍历的话，return 应该也写在前序位置」；「DFS 就不需要 return」
- **为什么错**：三件事是不同维度：「x 序」= 当前节点的事在递归前 / 中 / 后做；DFS / BFS = 访问顺序；末尾 `return x` = 父节点要不要这个值。前序遍历的分解写法 `return [root.val] + preorder(l) + preorder(r)` 是前序，但 `return` 最后执行；DFS 也可以靠返回值组合答案（`max(左, 右) + 1`）。
- **知识点**：遍历 vs 分解看「返回值能否被外部变量原样替换」；后来自己总结出了「末尾 return 取决于要不要回传值」✅
- **出处**：问答记录 Q54、Q57

### #48 · 700 searchBST：只走一边却沿用 `return left if left else right` → `UnboundLocalError`
- **时间**：2026-11-11 19:00
- **题目**：
  ```python
  if root.val > val:
      left = self.traverse(root.left, val)
  if root.val < val:
      right = self.traverse(root.right, val)
  return left if left else right
  ```
- **现象**：`[4,2,7,1,3]` 找 7 → `UnboundLocalError: cannot access local variable 'left'`；找 5 → `... 'right'`；找 2、1 正常
- **为什么错**：两个 `if` 只执行一个，另一个变量从未被赋值。最后一行是「两边都搜」旧版的写法，那时两个变量一定都有值。
- **正确写法**：分支里直接 `return self.searchBST(root.left, val)` / `return self.searchBST(root.right, val)`
- **知识点**：带返回值的递归，**每条路径都要按定义返回**；改写算法时，旧代码的每一行都要重新核对；`val: Optional(int)` → `val: int`（圆括号**第 5 次**）
- **出处**：问答记录 Q58

### #49 · 450 deleteNode：递归后没停 + 没接住返回值 → 树里出现环（MLE）；改版后又缺末尾 `return root`
- **时间**：2026-11-13 13:47（改版 13:51）
- **题目**：往左 / 往右用两个独立的 `if`，后面直接接「找到了，删除」；两个孩子都在时写 `self.deleteNode(root.right, target.val)`
- **现象**：示例 1（删 3）超出内存限制；本地打印发现节点 5 也被当成要删的节点，最后 `4.right is 4`
- **为什么错**：
  1. 去左边删完 3 后没 return，掉进下面的删除逻辑，把 5 也删了 → 三种情况应 `if / elif / else` 互斥。
  2. `deleteNode` 靠返回值交回新子树，结果没接住 → `root.right` 仍是 4 → `target.right = root.right` 变成 `4.right = 4`。
  3. 改版加了 `elif`，但左右分支走完后函数到末尾返回 None，整棵树丢失。
- **正确写法**：`root.right = self.deleteNode(root.right, target.val)`；函数最后补 `return root`（完整代码见 Q60 待办）
- **知识点**：「返回新的根」型递归：互斥分支 + 每条路径 return + 调用必接返回值；`getMin` 注解 `Optional(...)` **第 6 次**
- **出处**：问答记录 Q60

### #50 · 96 不同的 BST：不理解空树为什么返回 1
- **时间**：2026-11-13 15:46
- **题目**：`count(lo, hi)` 的 base case `if lo > hi: return 1`
- **卡点**：「没有数字」直觉上应该是 0 种
- **为什么是 1**：n = 1 倒推：`count(1,1) = count(1,0) × count(2,1)` 必须等于 1 → base case 只能是 1。`count` 数的是摆法不是节点数，空着本身是一种摆法；0 只表示不可能。乘法的中性元素是 1（加法是 0），和 98 的 `inf` / `-inf` 哨兵同理。
- **知识点**：计数问题的 base case 用「最小例子倒推」来确定
- **出处**：问答记录 Q61

### #51 · 以为 `path.copy()` 存的是 path 的地址；以为要用深拷贝
- **时间**：2026-11-13 17:50（17:54）
- **题目**：797 里 `self.res.append(self.path.copy())`，path 之后还会 append / pop
- **我的想法**：「这难道不应该用深拷贝？浅拷贝的话前面存的会被改变」；「copy 就是创建一个新对象，这个对象存储 path 的引用地址」
- **为什么错**：浅拷贝的新列表有**自己的格子**，格子里存的是 path **元素**的地址，和 path 本身没有连接。之后 path 增删的是自己的格子，新列表不受影响。path 里是不可变的整数，没人能修改元素，所以浅拷贝已经完全隔离。只有元素可变且会被原地修改时才需要深拷贝。
- **知识点**：浅拷贝 = 新容器 + 共享元素；`=` 换地址、方法改对象；对列表 `+=` 是原地修改（和 #1、#2、#3、#41 同一根源）
- **出处**：问答记录 Q64

### #52 · 「检测到 visited 就可以跳过」：漏了「先确认不在当前路径上」
- **时间**：2026-11-13 17:40
- **题目**：判环时碰到一个 visited 的节点 s，怎么处理？
- **我的想法**：「监测到 visited 之后，就可以跳过」
- **为什么不完整**：在当前路径上的节点也已经是 visited（进入时两个数组同时设 True）。visited 且 `onPath` 为 True → 有环；visited 且不在路上 → 才能跳过。如果先查 visited，`0→1→2→0` 走回 0 时直接 return，环就漏了。
- **正确写法**：先 `if onPath[s]: 有环`，再 `if visited[s]: return`
- **知识点**：两个条件重叠时，**判断顺序**决定结果；环 = 走回当前路径上的节点
- **出处**：问答记录 Q63

### #53 · 210 课程表：`reverted_res = self.res.reverse()` 拿到的是 None
- **时间**：2026-11-17 17:59
- **题目**：后序遍历结果倒过来就是拓扑排序：`reverted_res = self.res.reverse()`，然后 `return reverted_res if not self.hasCycle else []`
- **为什么错**：`list.reverse()` 是原地修改，返回 `None`（同 `sort`、`append`）
- **正确写法**：`self.res.reverse(); return self.res`，或 `return self.res[::-1]`
- **知识点**：原地修改的方法返回 None，别用它们的返回值（同类：#9 函数没 return）
- **出处**：问答记录 Q70（当时问题被打断，这段代码的其他部分还没逐行检查）

### #54 · 130 被围绕的区域：`connected` 比较的是 `parent`，不是根
- **时间**：2026-11-18 16:16
- **题目**：`rootP = self.parent[p]; rootQ = self.parent[q]; return rootP == rootQ`
- **现象**：35/59 通过；本地格子 `(1, 2)` 的 parent 是 7、根是 28，dummy 的根也是 28，却被判成不连通而改成 `X`
- **为什么错**：parent 不一定是根；路径压缩只在 `find` 时发生。样例树矮，parent 碰巧是根。
- **正确写法**：`return self.find(p) == self.find(q)`
- **知识点**：并查集判断连通 = 比较根；同一个类里 `union` 写对了，`connected` 没照着写（「碰巧对」）
- **出处**：问答记录 Q67

### #55 · 1584 Kruskal：`find` 的 base case 写了裸 `return`
- **时间**：2026-11-18 18:52
- **题目**：`if x == self.parent[x]: return`
- **现象**：所有 `find` 返回 None → `connected` 永远 True → 所有边被跳过 → `mst = 0`
- **为什么错**：`find` 的定义是返回根，base case 这条路径没交出值；裸 `return` = 返回 None
- **正确写法**：`return x`
- **知识点**：带返回值的递归，**base case 也要按定义返回**（同类 #48、#49）
- **出处**：问答记录 Q71

### #56 · 654 最大二叉树：右切片 `nums[maxIndex:n]` 把根也带进去 → 无限递归
- **时间**：2026-11-19 15:52
- **题目**：`right = self.constructMaximumBinaryTree(nums[maxIndex:n])`
- **现象**：超出时间限制（本地 `RecursionError`）；`[6,0,5]` 的 right 还是 `[6,0,5]`
- **为什么错**：最大值已经当了根，右子树区间应从 `maxIndex + 1` 开始；规模不缩小就永远到不了 base case
- **正确写法**：`nums[maxIndex+1:]`
- **知识点**：切片开闭区间（同 #4、#19）；**每次递归规模必须严格变小**
- **出处**：问答记录 Q72

### #57 · 以为 hash set 不存 value 就不用处理冲突
- **时间**：2026-11-20 10:49
- **我的想法**：「所以它不会解决 hash 冲突」
- **为什么错**：冲突发生在「key → 下标」这一步，和存不存 value 无关；set 和 dict 是同一套哈希表，CPython 用开放寻址，Java 用拉链法。例：`hash(-1) == hash(-2)`，但 `{-1, -2}` 两个都在。
- **知识点**：set ≈ 只有 key 的 dict；查找要 `__hash__` 定位 + `__eq__` 确认
- **出处**：问答记录 Q73

### #58 · 以为节点自己不是目标，最后就不用 `return left ... else right`
- **时间**：2026-11-20 11:35
- **题目**：LCA 前置 `find` 的最后一行 `return left if left is not None else right`
- **我的想法**：「左右子树都没有的话没有意义，直接弹栈向上再搜索就行，这个不用写」
- **为什么错**：找到的节点要一层层**转交**到最顶层；删掉后中间节点弹栈时带回 None，答案半路丢了
- **知识点**：「返回左右子树」= 转交孩子交上来的结果；末尾 return 取决于父节点要不要这个值（Q57，自己总结过但没用上）
- **出处**：问答记录 Q74

### #59 · 106 中序 + 后序建树：`num_of_left` 多 1；闭区间 base case 把单元素当成空
- **时间**：2026-11-20 15:44
- **题目**：`num_of_left = rootIndex - inStart + 1`；`if postStart >= postEnd: return None`
- **现象**：`RecursionError`；只修 base case 时输出 `[3, null, 20]`
- **为什么错**：① 根左边的个数是 `rootIndex - inStart`，多算 1 → 左子树把根分进去，规模不缩小；② 闭区间 `s == e` 有 1 个元素，`>=` 把所有叶子扔掉
- **正确写法**：`num_of_left = rootIndex - inStart`；`if postStart > postEnd: return None`
- **知识点**：off-by-one（同 #4、#56）；`Optional(TreeNode)` 圆括号**第 7 次**；`value_to_index = {}` 写成类变量（同 #40）
- **出处**：问答记录 Q75

### #60 · 106 第二版：base case 改成 `>=` 时建节点 → 空区间也建了节点
- **时间**：2026-11-20 15:57
- **题目**：`if postStart >= postEnd: return TreeNode(postorder[postEnd])`
- **现象**：示例 1 通过；`inorder = [1,2]`、`postorder = [1,2]` 输出 `[2, 1, 1]`（应为 `[2, 1]`）
- **为什么错**：`>=` 同时包含 1 个元素（`==`）和 0 个元素（`>`）。空区间 `post[1..0]` 也建了节点，值取 `post[0]`。示例 1 没有单孩子节点，碰巧没走到空区间。
- **正确写法**：`if postStart > postEnd: return None`，单元素照常走下去
- **知识点**：base case 写**真正为空**的条件；从「把 1 当 0」改成了「把 0 当 1」——改 bug 时要把两种情况都列出来核对；构造「只有一个孩子」的用例
- **出处**：问答记录 Q75

### #61 · 889 前序 + 后序建树：`right` 调用漏参数；没有单元素 base case
- **时间**：2026-11-20 19:37
- **题目**：`right = self.build(preorder, preStart+num_of_left+1, postorder, leftRootIndex+1, postEnd-1)`；只有 `if preStart >= preEnd: return None`
- **现象**：`IndexError: list index out of range`
- **为什么错**：① 漏了 `preEnd`（能走到这行会报 `TypeError: missing 1 required positional argument`）；② 单元素区间读 `preorder[preStart+1]`，拿到区间外的节点（叶子 4 读到兄弟 5），最后在叶子 7 越界
- **正确写法**：补 `preEnd`；加 `if preEnd - preStart == 1: return TreeNode(preorder[preStart])`
- **知识点**：递归只能读自己区间里的数据；进步：这次用了左闭右开且 base case 一致，`Optional[TreeNode]` 写对了 ✅
- **出处**：问答记录 Q76

### #62 · 以为单元素 base case 只是为了防越界 / 只有输入只有一个元素时才会出错
- **时间**：2026-11-20 19:43（19:45）
- **我的想法**：「是不是只有测试用例本身只有一个元素时才错？」「主要还是数组越界了，不然我也不用担心这个条件，对吧？」
- **为什么错**：任何树都有叶子，递归必然走到单元素区间；叶子 4、5、6 都没越界，但已经把兄弟、叔叔当成了孩子，结果是错的。越界只是假设不成立时偶尔冒出来的症状。
- **知识点**：写 base case 时问「下面的代码依赖哪些假设？什么时候不成立？」而不是「什么时候会崩」
- **出处**：问答记录 Q76

### #63 · 70 爬楼梯：辅助函数里递归调了入口函数 → dp 被反复重建
- **时间**：2026-11-23 15:14
- **题目**：`self.dp[n] = self.climbStairs(n-1) + self.climbStairs(n-2)`（应调 `self.__climbStairs`）
- **现象**：n = 3 正确；n = 4、5 → `IndexError: list assignment index out of range`
- **为什么错**：入口函数每次都 `self.dp = [-1]*(n+1)`，内层调用把 dp 换成更短的新列表，外层再写 `self.dp[n]` 就越界；备忘录也被清空。n = 3 的子调用在第一行就返回，碰巧没重建。
- **正确写法**：`self.dp[n] = self.__climbStairs(n-1) + self.__climbStairs(n-2)`
- **知识点**：入口初始化、辅助递归；**和 #43 完全同一个错误，第 2 次**
- **出处**：问答记录 Q77

### #64 · 354 LIS 二分：`mid` 写在 `while` 外面 → 死循环
- **时间**：2026-11-23 16:48
- **题目**：`mid = left + (right - left) // 2` 放在 `while left < right:` 之前
- **现象**：超时；高度 `[3, 4, 7, 4]` 处理最后一个 4 时 `left = 0, right = 1, mid = 1` 永远不变
- **为什么错**：mid 只算一次，left / right 变了它不跟着变；区间不再缩小
- **正确写法**：`while left < right:` 的第一行 `mid = (left + right) // 2`
- **知识点**：每轮要变的量写在循环里；赋值绑定的是那一刻的值（**和 #41 同一个根源，第 2 次**）；二分检查清单「每轮区间都在缩小吗」
- **出处**：问答记录 Q81

### #65 · 二分左边界的「为什么」第 2 次卡住（Q26 学过）
- **时间**：2026-11-23 16:38（18:01 想通）
- **题目**：`==` 时 `right = mid - 1`，后面再没有 `==` 了，为什么 `left` 还是左边界？
- **卡点**：靠逐轮模拟去理解，情况太多就没底；上次（Q26）的结论没留住
- **为什么**：循环不变量：`left` 左边全 < target、`right` 右边全 ≥ target；结束时 `left = right + 1` 就是第一个 ≥ target
- **知识点**：看循环先找不变量，不逐轮模拟；✅ 这次用不变量自己推出了右边界，说明真正掌握了
- **出处**：问答记录 Q80
