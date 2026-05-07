import os
TODO_LIST="todo.txt"
def load_tasks():
    if os.path.exists(TODO_LIST):
        return []
    with open(TODO_LIST,"r",encoding="utf-8")as f:
        tasks=[line.strip() for line in f.readlines()]
        return tasks
def save_tasks(tasks):
    with open(TODO_LIST,"w",encoding="utf-8")as f:
        for task in tasks:
            f.write(task+"\n")
def show_tasks(tasks):
    if not tasks:
        print("当前没有任务")
        return
    print("当前的任务是：")
    for i,task in enumerate(tasks):
        print(f"{i}. {task}")
def main():
    tasks = load_tasks()
    while True:
        print("\n有以下几个动作:show,add,delete,quit")
        cmd=input("请选择要操作的类型：")
        if cmd=="show":
            show_tasks(tasks)
        elif cmd=="add":
            task=input("请输入要添加的内容：").strip()
            if task:
                tasks.append(task)
                save_tasks(tasks)
                print(f"已添加{task}")
        elif cmd=="delete":
            show_tasks(tasks)
            index=input("请选择要删除的任务编号").strip()
            if index.isdigit():
                index=int(index)
                if 1<=index<=len(tasks):
                    removed = tasks.pop(index - int(index - 1))
                    save_tasks(tasks)
                    print(f"已删除{removed}")
                else:
                    print("请输入正确编号")
            else:
                print("请输入数字")
        elif cmd=="quit":
            print ("退出TODO LIST")
            break
        else:
            print("未知操作，请重试")
if __name__ == "__main__":
    main()
