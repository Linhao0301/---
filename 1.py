from graphviz import Digraph

def draw_ast():
    # 创建一个Digraph对象
    dot = Digraph()

    # 添加节点
    dot.node('A', '+')
    dot.node('B', 'a')
    dot.node('C', '-')
    dot.node('D', '+')
    dot.node('E', 'b')
    dot.node('F', 'c')

    # 添加边，定义树的结构
    dot.edge('A', 'B')
    dot.edge('A', 'C')
    dot.edge('C', 'D')
    dot.edge('D', 'E')
    dot.edge('D', 'F')

    # 渲染和查看图形
    dot.render('ast.gv', view=True)

draw_ast()
