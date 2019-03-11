"""
    功能：分形树绘制
    新功能：利用递归绘制分形树
    新功能：分形树
"""
import turtle


def draw_brunch(br_len, len_step, deg):
    """
        绘制分形数
    """
    if br_len > 5:
        # 绘制右侧树枝
        turtle.forward(br_len)
        turtle.right(deg)
        draw_brunch(br_len-len_step, len_step, deg)

        turtle.left(deg * 2)
        # 绘制左侧树枝
        draw_brunch(br_len - len_step, len_step, deg)

        # 返回之前树枝
        turtle.right(deg)
        turtle.backward(br_len)


def main():
    """
        主函数
    """
    turtle.left(90)
    turtle.penup()
    turtle.backward(200)
    turtle.pendown()

    length = 50
    deg = 25
    len_step = 10
    draw_brunch(length, len_step, deg)

    turtle.exitonclick()


if __name__ == '__main__':
        main()

