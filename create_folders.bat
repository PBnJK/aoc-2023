CD src

FOR /L %%i in (1,1,25) DO (
	IF %%i LSS 10 (
		CD day0%%i
	) ELSE (
		CD day%%i
	)
	
	TYPE NUL > input.txt
	CD ..
)