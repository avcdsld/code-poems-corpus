function you(now)
! Oh !
logical you
! already
now=now+1
if (now ==6) you=.false.
! you never
return
end

program endet
logical dream
logical night
logical you
!!
character*3 me
me='ill'

now=0
night=.true.
! I toss and turn and
do while(night)
    dream = you(now)
    night=dream
    !Oh yes, please
    write(*,*) dream, me
    ! On the sheets
    write(*,*)' me with your',night,'ire: ', now
enddo
end
