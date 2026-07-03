# 文档字符串
# 文档字符串是用来描述模块、类、函数、方法等内容的字符串，通常用于解释代码的作用、参数、返回值等
# 文档字符串使用三引号（''' 或 """）来定义，通常位于模块、类、函数、方法的第一个位置

# 获取方式：
# 1. 使用__doc__属性
# 2. 使用help()函数,会多输出函数所在的模块，函数声明
# 3. 使用inspect模块

# 文档字符串规范：
# 1. Google风格
## a. 第一行，一句话摘要，以动词开头，比如Add/Update/Create/Fetch...
## b. 第二段，描述函数的作用
## c. 第三段，分节说明，常见为Args/Returns/Raises/Examples
# 2. Numpy风格（和Google风格类似）

## 示例：函数文档字符串

def fetch_user_profiles(user_id: str, *, include_posts: bool = False) -> dict: 
    """Fetch user profiles from the remote service.

    Retriveves basic user infomation and optionally includes posts.

    Args:
        user_id: The ID of the user to fetch.
        include_posts: Whether to include posts in the response.

    Returns:
        A dictionary containing user infomation and posts. Example:
        {"user_id": "123", "name": "John Doe", "email": "john.doe@example.com", "posts": [...]}

    Raises:
        ValueError: If the user_id is not valid.
        TimeoutError: If the request times out.
    """
    if not user_id: 
        raise ValueError("user_id is required")
    #...

    return {"user_id": user_id, "name": "John Doe", "email": "john.doe@example.com", "posts": [] if include_posts else None}

# 获取docs_string
print('===============__doc__===========')
print(fetch_user_profiles.__doc__)

print('===========================help()===========================')
print(help(fetch_user_profiles))

print('===========================inspect.getdoc()===========================')
import inspect
print(inspect.getdoc(fetch_user_profiles))