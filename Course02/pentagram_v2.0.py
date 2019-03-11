"""
    功能：五角星绘制
    新功能：递归
"""
import turtle


def draw_recursive_pentagram(size):
    """
       迭代绘制画五角星
    """
    count = 1
    while count <= 5:
        count += 1
        turtle.pencolor("red")
        turtle.forward(size)
        turtle.right(144)

    # 五角星绘制完成，更新参数
    size += 10
    if size <= 100:
        draw_recursive_pentagram(size)


def main():
    """
        主函数
    """
    turtle.penup()
    turtle.backward(50)
    turtle.pendown()

    size = 50
    draw_recursive_pentagram(size)

    turtle.exitonclick()


if __name__ == '__main__':
        main()

