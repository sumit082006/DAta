class TextEditor:
    def __init__(self):
        self.document = ""
        self.undo_stack = []
        self.redo_stack = []

    # 1. Make a change
    def make_change(self, new_text):
        # Save current state before making the change
        self.undo_stack.append(self.document)

        # Update document
        self.document = new_text

        # New changes invalidate the redo history
        self.redo_stack.clear()

        print("Change made:", self.document)

    # 2. Undo action
    def undo(self):
        if not self.undo_stack:
            print("Nothing to undo!")
            return

        # Save current state for redo
        self.redo_stack.append(self.document)

        # Restore previous state
        self.document = self.undo_stack.pop()

        print("Undo:", self.document)

    # 3. Redo action
    def redo(self):
        if not self.redo_stack:
            print("Nothing to redo!")
            return

        # Save current state for undo
        self.undo_stack.append(self.document)

        # Restore the most recently undone state
        self.document = self.redo_stack.pop()

        print("Redo:", self.document)

    # 4. Display document state
    def display(self):
        print("Current Document:", self.document)


# -------------------------------
# Example usage
# -------------------------------

editor = TextEditor()

editor.make_change("Hello")
editor.make_change("Hello World")
editor.make_change("Hello World!")

editor.display()

editor.undo()
editor.display()

editor.undo()
editor.display()

editor.redo()
editor.display()

editor.redo()
editor.display()
editor.display()