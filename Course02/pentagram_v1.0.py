"""
    功能：五角星绘制
"""
import turtle


def draw_pentagram(size):
    """
        画五角星
    """
    count = 1
    while count <= 5:
        count += 1
        turtle.pencolor("red")
        turtle.forward(size)
        turtle.right(144)


def main():
    """
        主函数
    """
    turtle.penup()
    turtle.backward(50)
    turtle.pendown()


    len = 100
    while len <= 300:
        # 调用画五角星函数
        draw_pentagram(len)
        len += 50

    turtle.exitonclick()


if __name__ == '__main__':
        main()

