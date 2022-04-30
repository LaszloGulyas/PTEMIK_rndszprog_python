from application.controller.record_editor_controller import RecordEditorController

if __name__ == '__main__':
    print('Application starting...')
    main_controller = RecordEditorController()
    main_controller.create_view()

