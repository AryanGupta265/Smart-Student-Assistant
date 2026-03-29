low_attendance(Attendance) :-
    Attendance < 75.

low_marks(Marks) :-
    Marks < 60.

suggestion(Attendance, Marks, Advice) :-
    low_attendance(Attendance),
    Advice = 'Improve your attendance'.

suggestion(Attendance, Marks, Advice) :-
    low_marks(Marks),
    Advice = 'Study more and practice daily'.

suggestion(Attendance, Marks, Advice) :-
    Attendance >= 75,
    Marks >= 60,
    Advice = 'You are doing well, keep it up!'.
