import random

class Hat:
    def __init__(self, **balls):
        self.contents = []
        for color, count in balls.items():
            self.contents.extend([color] * count)
    
    def draw(self, num_balls):
        if num_balls >= len(self.contents):
            drawn = self.contents.copy()
            self.contents.clear()
            return drawn
        drawn = random.sample(self.contents, num_balls)
        for ball in drawn:
            self.contents.remove(ball)
        return drawn

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    successes = 0
    
    for _ in range(num_experiments):
        # Create a copy of the hat for each experiment
        hat_copy = Hat()
        hat_copy.contents = list(hat.contents)
        
        # Draw balls
        drawn = hat_copy.draw(num_balls_drawn)
        
        # Count how many of each color we got
        drawn_counts = {}
        for color in drawn:
            drawn_counts[color] = drawn_counts.get(color, 0) + 1
        
        # Check if we got at least the expected balls
        success = True
        for color, count in expected_balls.items():
            if drawn_counts.get(color, 0) < count:
                success = False
                break
        
        if success:
            successes += 1
    
    return successes / num_experiments

# Test case that was failing
print("Testing draw with more balls than in hat:")
test_hat = Hat(red=3)
print("Initial contents:", test_hat.contents)
drawn = test_hat.draw(5)  # Trying to draw 5 when only 3 exist
print("Drawn balls:", drawn)
print("Remaining contents:", test_hat.contents)
print("Length of drawn balls:", len(drawn))