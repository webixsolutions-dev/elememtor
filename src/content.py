"""Sample 'Did You Know' stories (WordPress posts) so the dynamic templates look
exactly like the mockups right after import."""
from pages import img

CATEGORIES = [("ingredient-origins", "Ingredient Origins"), ("kitchen-tips", "Kitchen Tips")]

TURMERIC_BODY = f"""<!-- wp:heading -->
<h2 class="wp-block-heading">A golden ingredient for everyday cooking</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Turmeric is a vibrant, golden root that brings warm color and earthy flavor to everyday meals. Its distinctive taste pairs beautifully with a wide range of ingredients, making it a versatile addition to both simple and creative cooking.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Whether you’re adding it to a comforting soup, stirring it into rice, or blending it into a creamy drink, turmeric is an easy way to bring more flavor and color to your kitchen.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2 class="wp-block-heading">Simple ways to use turmeric</h2>
<!-- /wp:heading -->

<!-- wp:list -->
<ul class="wp-block-list"><!-- wp:list-item -->
<li><strong>In rice:</strong> Stir a pinch of turmeric powder into rice or grains for a beautiful golden color and subtle, earthy flavor.</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li><strong>In soups:</strong> Add turmeric to soups, stews or curries to bring depth and warmth to your dishes.</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li><strong>In warm drinks:</strong> Mix turmeric into warm milk or your favorite plant-based alternative for a cozy, golden drink.</li>
<!-- /wp:list-item --></ul>
<!-- /wp:list -->

<!-- wp:image {{"sizeSlug":"large"}} -->
<figure class="wp-block-image size-large"><img src="{img('post-golden-latte')}" alt="Golden turmeric latte in a ceramic mug with turmeric powder and fresh roots"/></figure>
<!-- /wp:image -->

<!-- wp:heading -->
<h2 class="wp-block-heading">Golden latte inspiration</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>A golden latte is a comforting and flavorful way to enjoy turmeric. Simply whisk a pinch of turmeric powder into warm milk or your favorite plant-based alternative, add a touch of cinnamon, and sweeten to taste. It’s a simple, cozy drink that’s perfect for any time of day.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2 class="wp-block-heading">Keeping it fresh</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Store turmeric powder in an airtight container in a cool, dry place, away from direct sunlight. This helps keep its vibrant color and flavor fresh for longer, so it’s always ready when you need it.</p>
<!-- /wp:paragraph -->"""


def _simple_body(sections):
    out = []
    for h, paras in sections:
        out.append(f'<!-- wp:heading -->\n<h2 class="wp-block-heading">{h}</h2>\n<!-- /wp:heading -->')
        for p in paras:
            out.append(f"<!-- wp:paragraph -->\n<p>{p}</p>\n<!-- /wp:paragraph -->")
    return "\n\n".join(out)


POSTS = [
    {
        "slug": "meet-turmeric", "title": "Meet turmeric: color, flavor & kitchen inspiration",
        "date": "2026-09-30 09:00:00", "cat": "ingredient-origins", "image": "post-turmeric-hero",
        "excerpt": "A closer look at this vibrant root, its distinctive flavor, and simple ways to use it in everyday meals and drinks.",
        "subtitle": "A closer look at this golden kitchen staple.", "eyebrow": "Ingredient Spotlight",
        "read": "5 min read", "body": TURMERIC_BODY,
    },
    {
        "slug": "getting-to-know-moringa", "title": "Getting to know moringa",
        "date": "2026-09-26 09:00:00", "cat": "ingredient-origins", "image": "story-moringa",
        "excerpt": "Discover the origins, flavor and simple ways to enjoy moringa powder in your everyday kitchen.",
        "subtitle": "The bright green leaf with a fresh, earthy taste.", "eyebrow": "Ingredient Origins",
        "read": "4 min read",
        "body": _simple_body([
            ("Where moringa comes from", [
                "Moringa grows in warm climates, where its small, tender leaves are harvested, gently dried and milled into a fine green powder.",
                "The result is a vivid ingredient with a fresh, slightly grassy flavor that blends easily into everyday recipes."]),
            ("Simple ways to enjoy it", [
                "Whisk a spoonful into smoothies, stir it through yogurt or oat bowls, or fold it into pancake batter for a beautiful green color."]),
            ("Keeping it fresh", [
                "Keep moringa sealed in its pouch or an airtight jar, away from heat and light, to protect its color and flavor."]),
        ]),
    },
    {
        "slug": "beetroot-beyond-the-salad-bowl", "title": "Beetroot beyond the salad bowl",
        "date": "2026-09-22 09:00:00", "cat": "kitchen-tips", "image": "story-beetroot",
        "excerpt": "A closer look at beetroot powder and easy, creative ways to use it in drinks, baked goods and more.",
        "subtitle": "Naturally vibrant color for drinks, bakes and dips.", "eyebrow": "Kitchen Tips",
        "read": "4 min read",
        "body": _simple_body([
            ("A naturally vibrant ingredient", [
                "Beetroot powder brings a deep ruby color and gentle, earthy sweetness to your kitchen without any fuss.",
                "A little goes a long way, so start with a small spoonful and build from there."]),
            ("Creative ways to use it", [
                "Blend it into smoothies, swirl it through hummus, or add it to frosting and baked goods for a naturally pink finish."]),
        ]),
    },
    {
        "slug": "ginger-in-your-everyday-kitchen", "title": "Ginger in your everyday kitchen",
        "date": "2026-09-18 09:00:00", "cat": "kitchen-tips", "image": "story-ginger",
        "excerpt": "Explore the warm, aromatic flavor of ginger powder and simple ideas for adding it to your daily recipes.",
        "subtitle": "Warm, aromatic and endlessly useful.", "eyebrow": "Kitchen Tips", "read": "3 min read",
        "body": _simple_body([
            ("Warm and aromatic", [
                "Ground ginger has a bright, warming flavor that works in both sweet and savory dishes.",
                "It’s a pantry staple that adds instant depth to everyday cooking."]),
            ("Everyday ideas", [
                "Add it to stir-fries and marinades, bake it into cookies and loaves, or stir a pinch into hot water with lemon."]),
        ]),
    },
    {
        "slug": "from-cacao-bean-to-powder", "title": "From cacao bean to powder",
        "date": "2026-09-14 09:00:00", "cat": "ingredient-origins", "image": "story-cacao",
        "excerpt": "Follow the journey from cacao bean to powder, and find everyday ways to enjoy its rich, chocolatey flavor.",
        "subtitle": "The rich, chocolatey story behind every spoonful.", "eyebrow": "Ingredient Origins",
        "read": "5 min read",
        "body": _simple_body([
            ("The journey of the bean", [
                "Cacao pods are harvested, and their beans are fermented, dried and gently processed before being milled into a fine powder.",
                "Each step shapes the deep, chocolatey flavor that makes cacao so loved."]),
            ("Ways to enjoy it", [
                "Stir it into warm drinks, blend it into smoothies, or use it in brownies, energy bites and breakfast bowls."]),
        ]),
    },
    {
        "slug": "simple-smoothie-inspiration", "title": "Simple smoothie inspiration",
        "date": "2026-09-10 09:00:00", "cat": "kitchen-tips", "image": "story-smoothie",
        "excerpt": "Easy, delicious smoothie ideas using natural plant powders for a colorful start to your day.",
        "subtitle": "Colorful blends for a bright start to the day.", "eyebrow": "Kitchen Tips", "read": "3 min read",
        "body": _simple_body([
            ("Build a better blend", [
                "Start with a base of fruit and your favorite milk, then add a spoonful of plant powder for color and flavor.",
                "Moringa pairs beautifully with banana and pineapple, while beetroot loves berries."]),
            ("Our favorite combinations", [
                "Try moringa, mango and lime; beetroot, strawberry and oat; or cacao, banana and peanut butter."]),
        ]),
    },
    {
        "slug": "storing-your-pantry-powders", "title": "Storing your pantry powders",
        "date": "2026-09-06 09:00:00", "cat": "kitchen-tips", "image": "story-pantry",
        "excerpt": "Simple tips for keeping your plant powders fresh, organized and ready for everyday use.",
        "subtitle": "Keep color and flavor at their best.", "eyebrow": "Kitchen Tips", "read": "3 min read",
        "body": _simple_body([
            ("Cool, dry and dark", [
                "Light, heat and moisture are the main enemies of plant powders. Keep them in airtight containers in a cool cupboard.",
                "Always use a dry spoon to avoid clumping."]),
            ("Stay organized", [
                "Label your jars with the powder name and opening date, and keep your everyday favorites at the front of the shelf."]),
        ]),
    },
]
