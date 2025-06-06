def check_collision(ball, paddle, bricks):
    score_increment = 0  # Track the score increment

    # Ball colliding with paddle
    if paddle.position[1] <= ball.position[1] + ball.radius <= paddle.position[1] + 10 and \
            paddle.position[0] <= ball.position[0] <= paddle.position[0] + paddle.width:
        ball.direction[1] *= -1  # Reverse the ball's direction

    # Ball colliding with bricks
    for brick in bricks:
        if brick.alive and brick.position[0] <= ball.position[0] <= brick.position[0] + brick.width and \
                brick.position[1] <= ball.position[1] <= brick.position[1] + brick.height:
            brick.alive = False  # Remove brick
            ball.direction[1] *= -1  # Reverse ball direction
            score_increment += 1  # Increase score count
    return score_increment
