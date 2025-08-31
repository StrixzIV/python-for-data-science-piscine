import time

current_time_epoch = time.time()

print(f'Seconds since January 1, 1970: {current_time_epoch:,.4f} or {current_time_epoch:.2e} in scientific notation')
print(time.strftime("%B %e %Y"))
